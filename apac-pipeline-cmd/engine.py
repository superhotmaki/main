"""
Pipeline consolidation engine.
Takes raw deals from all entities and produces a unified consolidated view
with aggregations, forecasts, risk analysis, and trend data.
"""
from datetime import datetime, timedelta
from collections import defaultdict
from models import (
    Entity, Currency, Stage, Vertical, Deal,
    EntitySummary, ConsolidatedPipeline, ENTITY_CURRENCY, STAGE_WEIGHTS
)
from currency import CurrencyEngine
from datagen import DataGenerator


class PipelineEngine:
    """Core engine that consolidates pipeline data across all APAC entities."""

    def __init__(self, deals: list = None, seed: int = 42):
        self.currency_engine = CurrencyEngine(seed=seed)

        if deals is None:
            gen = DataGenerator(seed=seed)
            self.deals = gen.generate_full_pipeline()
            self.datagen = gen
        else:
            self.deals = deals
            self.datagen = DataGenerator(seed=seed)

    def get_entity_summary(self, entity: Entity) -> EntitySummary:
        """Compute summary metrics for a single entity."""
        entity_deals = [d for d in self.deals if d.entity == entity]
        currency = ENTITY_CURRENCY[entity]

        if not entity_deals:
            return EntitySummary(
                entity=entity, currency=currency, total_deals=0,
                total_local_value=0, total_usd_value=0, weighted_pipeline=0,
                deals_by_stage={}, avg_deal_size_usd=0, largest_deal_usd=0,
                conversion_rate=0, velocity_days=0
            )

        total_local = sum(d.local_value for d in entity_deals)
        total_usd = sum(d.usd_value for d in entity_deals)
        weighted = sum(d.usd_value * d.probability for d in entity_deals)

        # Deals by stage
        by_stage = {}
        for stage in Stage:
            stage_deals = [d for d in entity_deals if d.stage == stage]
            by_stage[stage.value] = {
                "count": len(stage_deals),
                "total_usd": round(sum(d.usd_value for d in stage_deals), 2),
            }

        avg_size = total_usd / len(entity_deals) if entity_deals else 0
        largest = max(d.usd_value for d in entity_deals) if entity_deals else 0

        # Conversion rate
        won = len([d for d in entity_deals if d.stage == Stage.CLOSED_WON])
        lost = len([d for d in entity_deals if d.stage == Stage.CLOSED_LOST])
        conv_rate = won / (won + lost) if (won + lost) > 0 else 0

        # Velocity: average days from creation to expected close for closed deals
        closed = [d for d in entity_deals if d.stage in (Stage.CLOSED_WON, Stage.CLOSED_LOST)]
        if closed:
            velocities = []
            for d in closed:
                created = datetime.strptime(d.created_date, "%Y-%m-%d")
                close = datetime.strptime(d.expected_close, "%Y-%m-%d")
                velocities.append(abs((close - created).days))
            velocity = sum(velocities) / len(velocities)
        else:
            velocity = 0

        return EntitySummary(
            entity=entity,
            currency=currency,
            total_deals=len(entity_deals),
            total_local_value=total_local,
            total_usd_value=total_usd,
            weighted_pipeline=weighted,
            deals_by_stage=by_stage,
            avg_deal_size_usd=avg_size,
            largest_deal_usd=largest,
            conversion_rate=conv_rate,
            velocity_days=velocity,
        )

    def get_stage_summary(self) -> dict:
        """Aggregate pipeline by stage across all entities."""
        summary = {}
        for stage in Stage:
            stage_deals = [d for d in self.deals if d.stage == stage]
            summary[stage.value] = {
                "count": len(stage_deals),
                "total_usd": round(sum(d.usd_value for d in stage_deals), 2),
                "weighted_usd": round(sum(d.usd_value * d.probability for d in stage_deals), 2),
                "avg_deal_size": round(
                    sum(d.usd_value for d in stage_deals) / len(stage_deals), 2
                ) if stage_deals else 0,
                "entities": list(set(d.entity.name for d in stage_deals)),
            }
        return summary

    def get_vertical_summary(self) -> dict:
        """Aggregate pipeline by vertical across all entities."""
        summary = {}
        for vertical in Vertical:
            v_deals = [d for d in self.deals if d.vertical == vertical]
            entity_breakdown = {}
            for entity in Entity:
                e_deals = [d for d in v_deals if d.entity == entity]
                if e_deals:
                    entity_breakdown[entity.name] = {
                        "count": len(e_deals),
                        "total_usd": round(sum(d.usd_value for d in e_deals), 2),
                    }

            summary[vertical.value] = {
                "count": len(v_deals),
                "total_usd": round(sum(d.usd_value for d in v_deals), 2),
                "weighted_usd": round(sum(d.usd_value * d.probability for d in v_deals), 2),
                "entities": entity_breakdown,
            }
        return summary

    def get_top_deals(self, n: int = 10) -> list:
        """Get top N deals by USD value (excluding closed lost)."""
        active = [d for d in self.deals if d.stage != Stage.CLOSED_LOST]
        sorted_deals = sorted(active, key=lambda d: d.usd_value, reverse=True)
        return [d.to_dict() for d in sorted_deals[:n]]

    def get_at_risk_deals(self, stale_days: int = 30) -> list:
        """Get deals with no activity in N+ days (excluding closed)."""
        today = datetime(2026, 2, 25)
        cutoff = today - timedelta(days=stale_days)
        cutoff_str = cutoff.strftime("%Y-%m-%d")

        at_risk = [
            d for d in self.deals
            if d.stage not in (Stage.CLOSED_WON, Stage.CLOSED_LOST)
            and d.last_activity < cutoff_str
        ]
        sorted_risk = sorted(at_risk, key=lambda d: d.usd_value, reverse=True)
        return [d.to_dict() for d in sorted_risk]

    def get_forecast(self) -> dict:
        """Generate pipeline forecast for next 3 months."""
        today = datetime(2026, 2, 25)
        active_deals = [
            d for d in self.deals
            if d.stage not in (Stage.CLOSED_WON, Stage.CLOSED_LOST)
        ]

        forecast = {}
        for months_ahead in [1, 2, 3]:
            cutoff = today + timedelta(days=months_ahead * 30)
            cutoff_str = cutoff.strftime("%Y-%m-%d")

            in_window = [d for d in active_deals if d.expected_close <= cutoff_str]
            total = sum(d.usd_value for d in in_window)
            weighted = sum(d.usd_value * d.probability for d in in_window)
            deal_count = len(in_window)

            month_label = (today + timedelta(days=months_ahead * 30)).strftime("%Y-%m")
            forecast[month_label] = {
                "deals": deal_count,
                "total_usd": round(total, 2),
                "weighted_usd": round(weighted, 2),
                "by_entity": {},
            }

            for entity in Entity:
                e_deals = [d for d in in_window if d.entity == entity]
                if e_deals:
                    forecast[month_label]["by_entity"][entity.name] = {
                        "deals": len(e_deals),
                        "total_usd": round(sum(d.usd_value for d in e_deals), 2),
                        "weighted_usd": round(sum(d.usd_value * d.probability for d in e_deals), 2),
                    }

        return forecast

    def consolidate(self) -> ConsolidatedPipeline:
        """Produce the full consolidated pipeline view."""
        entities = [self.get_entity_summary(e).to_dict() for e in Entity]
        deals = [d.to_dict() for d in self.deals]
        stage_summary = self.get_stage_summary()
        vertical_summary = self.get_vertical_summary()
        monthly_trend = self.datagen.generate_monthly_history(self.deals, months=12)
        top_deals = self.get_top_deals(15)
        at_risk = self.get_at_risk_deals(30)
        forecast = self.get_forecast()
        currency_rates = self.currency_engine.get_all_rates()

        total_usd = sum(d.usd_value for d in self.deals)
        weighted_usd = sum(d.usd_value * d.probability for d in self.deals)

        return ConsolidatedPipeline(
            generated_at=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            reporting_currency="USD",
            total_deals=len(self.deals),
            total_pipeline_usd=total_usd,
            weighted_pipeline_usd=weighted_usd,
            entities=entities,
            deals=deals,
            stage_summary=stage_summary,
            vertical_summary=vertical_summary,
            currency_rates=currency_rates,
            monthly_trend=monthly_trend,
            top_deals=top_deals,
            at_risk_deals=at_risk,
            forecast=forecast,
        )


if __name__ == "__main__":
    engine = PipelineEngine()
    result = engine.consolidate()
    print(f"Consolidated pipeline: {result.total_deals} deals")
    print(f"Total pipeline: ${result.total_pipeline_usd:,.0f} USD")
    print(f"Weighted pipeline: ${result.weighted_pipeline_usd:,.0f} USD")
    print(f"\nEntity breakdown:")
    for e in result.entities:
        print(f"  {e['entity_label']}: {e['total_deals']} deals, ${e['total_usd_value']:,.0f}")
    print(f"\nAt-risk deals: {len(result.at_risk_deals)}")
    print(f"Top deal: {result.top_deals[0]['name']} (${result.top_deals[0]['usd_value']:,.0f})")
