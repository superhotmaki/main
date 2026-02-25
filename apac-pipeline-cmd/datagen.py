"""
Synthetic data generator for APAC Pipeline Command Center.
Generates realistic-looking pipeline data across 8 APAC entities.
"""
import random
from datetime import datetime, timedelta
from models import (
    Entity, Currency, Stage, Vertical, Deal,
    ENTITY_CURRENCY, STAGE_WEIGHTS
)
from currency import CurrencyEngine


# Realistic company name fragments per market
COMPANY_PREFIXES = {
    Entity.AU: ["Southern Cross", "Pacific", "Outback", "Harbour", "Blue Sky", "Kookaburra", "Reef"],
    Entity.JP: ["Sakura", "Yamato", "Nikkei", "Kaze", "Hikari", "Mizu", "Fuji"],
    Entity.SG: ["Lion City", "Merlion", "Marina", "Orchid", "Garden", "Strait", "Temasek"],
    Entity.HK: ["Victoria", "Dragon", "Peak", "Jade", "Star Ferry", "Harbour View", "Golden"],
    Entity.KR: ["Hangang", "Arirang", "Cheonsa", "Baram", "Hallyu", "Nara", "Seonbi"],
    Entity.IN: ["Namaste", "Lotus", "Ganges", "Monsoon", "Spice Route", "Dharma", "Banyan"],
    Entity.TH: ["Siam", "Golden Temple", "Lotus", "Chao Phraya", "Jasmine", "Teak", "Emerald"],
    Entity.ID: ["Nusantara", "Garuda", "Batik", "Candi", "Krakatoa", "Komodo", "Borobudur"],
}

COMPANY_SUFFIXES = [
    "Technologies", "Solutions", "Systems", "Digital", "Analytics",
    "Cloud", "Platforms", "Labs", "Group", "Ventures",
    "Networks", "Capital", "Holdings", "Corp", "Inc",
]

# Deal type modifiers
DEAL_TYPES = [
    "Platform Migration", "Cloud Deployment", "Analytics Suite",
    "API Integration", "Data Lake", "Security Upgrade",
    "Mobile Rollout", "AI Implementation", "Compliance System",
    "Infrastructure Modernization", "DevOps Pipeline",
    "Customer Portal", "Payment Gateway", "ERP Integration",
    "Supply Chain Platform", "Risk Engine", "Trading System",
]

# Owner names per entity
OWNERS = {
    Entity.AU: ["James Chen", "Sarah Mitchell", "David Wong", "Emma Torres"],
    Entity.JP: ["Takeshi Yamada", "Yuki Tanaka", "Kenji Sato", "Mika Suzuki"],
    Entity.SG: ["Wei Lin Tan", "Priya Kumar", "Marcus Lee", "Rachel Ng"],
    Entity.HK: ["Michael Chan", "Jenny Liu", "Raymond Ho", "Karen Tsang"],
    Entity.KR: ["Min-jun Park", "Seo-yeon Kim", "Jun-ho Lee", "Ha-eun Choi"],
    Entity.IN: ["Rahul Sharma", "Priyanka Patel", "Vikram Singh", "Ananya Gupta"],
    Entity.TH: ["Somchai Wattana", "Nattaya Sriwan", "Arthit Chai", "Ploy Suk"],
    Entity.ID: ["Budi Santoso", "Dewi Putri", "Andi Prasetyo", "Siti Rahayu"],
}

# Deal size ranges in local currency (rough equivalents)
LOCAL_DEAL_RANGES = {
    Entity.AU: (30_000, 3_000_000),
    Entity.JP: (5_000_000, 500_000_000),
    Entity.SG: (40_000, 4_000_000),
    Entity.HK: (200_000, 20_000_000),
    Entity.KR: (40_000_000, 4_000_000_000),
    Entity.IN: (2_000_000, 200_000_000),
    Entity.TH: (1_000_000, 100_000_000),
    Entity.ID: (500_000_000, 50_000_000_000),
}


class DataGenerator:
    """Generates synthetic but realistic APAC pipeline data."""

    def __init__(self, seed=42):
        self.rng = random.Random(seed)
        self.currency_engine = CurrencyEngine(seed=seed)
        self.deal_counter = 0

    def generate_deal(self, entity: Entity, stage: Stage = None, vertical: Vertical = None) -> Deal:
        """Generate a single realistic deal for an entity."""
        self.deal_counter += 1
        currency = ENTITY_CURRENCY[entity]

        # Pick random attributes
        if stage is None:
            # Weight toward earlier stages (more prospects than closed)
            stage_weights = [0.25, 0.20, 0.20, 0.15, 0.12, 0.08]
            stage = self.rng.choices(list(Stage), weights=stage_weights, k=1)[0]

        if vertical is None:
            vertical = self.rng.choice(list(Vertical))

        # Generate deal value in local currency
        lo, hi = LOCAL_DEAL_RANGES[entity]
        # Log-normal distribution for more realistic deal sizes
        log_lo, log_hi = __import__('math').log(lo), __import__('math').log(hi)
        local_value = __import__('math').exp(self.rng.uniform(log_lo, log_hi))

        # Round nicely
        if local_value > 1_000_000:
            local_value = round(local_value / 100_000) * 100_000
        elif local_value > 10_000:
            local_value = round(local_value / 1_000) * 1_000
        else:
            local_value = round(local_value / 100) * 100

        usd_value = self.currency_engine.convert_to_usd(local_value, currency)

        # Generate dates
        today = datetime(2026, 2, 25)
        created_offset = self.rng.randint(30, 365)
        created_date = today - timedelta(days=created_offset)

        if stage in (Stage.CLOSED_WON, Stage.CLOSED_LOST):
            close_offset = self.rng.randint(0, created_offset - 10)
            expected_close = today - timedelta(days=close_offset)
        else:
            close_offset = self.rng.randint(14, 180)
            expected_close = today + timedelta(days=close_offset)

        # Last activity: recent for active deals, older for stale ones
        if self.rng.random() < 0.2:  # 20% chance of being stale
            activity_offset = self.rng.randint(31, 90)
        else:
            activity_offset = self.rng.randint(0, 14)
        last_activity = today - timedelta(days=activity_offset)

        # Probability based on stage + some randomness
        base_prob = STAGE_WEIGHTS[stage]
        prob_noise = self.rng.uniform(-0.05, 0.05)
        probability = max(0.0, min(1.0, base_prob + prob_noise))

        # Company name
        prefix = self.rng.choice(COMPANY_PREFIXES[entity])
        suffix = self.rng.choice(COMPANY_SUFFIXES)
        company = f"{prefix} {suffix}"

        # Deal name
        deal_type = self.rng.choice(DEAL_TYPES)
        name = f"{company} - {deal_type}"

        owner = self.rng.choice(OWNERS[entity])

        deal_id = f"DEAL-{entity.name}-{self.deal_counter:04d}"

        return Deal(
            id=deal_id,
            name=name,
            entity=entity,
            currency=currency,
            local_value=local_value,
            usd_value=usd_value,
            stage=stage,
            vertical=vertical,
            owner=owner,
            created_date=created_date.strftime("%Y-%m-%d"),
            expected_close=expected_close.strftime("%Y-%m-%d"),
            last_activity=last_activity.strftime("%Y-%m-%d"),
            probability=round(probability, 2),
        )

    def generate_entity_pipeline(self, entity: Entity, num_deals: int = None) -> list:
        """Generate a full pipeline for one entity."""
        if num_deals is None:
            # Larger markets get more deals
            market_sizes = {
                Entity.AU: (25, 40),
                Entity.JP: (30, 50),
                Entity.SG: (20, 35),
                Entity.HK: (15, 30),
                Entity.KR: (20, 40),
                Entity.IN: (30, 55),
                Entity.TH: (15, 25),
                Entity.ID: (20, 35),
            }
            lo, hi = market_sizes[entity]
            num_deals = self.rng.randint(lo, hi)

        return [self.generate_deal(entity) for _ in range(num_deals)]

    def generate_full_pipeline(self) -> list:
        """Generate pipeline data for all 8 APAC entities."""
        all_deals = []
        for entity in Entity:
            deals = self.generate_entity_pipeline(entity)
            all_deals.extend(deals)
        return all_deals

    def generate_monthly_history(self, deals: list, months: int = 12) -> list:
        """Generate monthly pipeline snapshots for trend analysis."""
        today = datetime(2026, 2, 25)
        history = []

        for i in range(months, -1, -1):
            month_date = today - timedelta(days=i * 30)
            month_str = month_date.strftime("%Y-%m")

            # Filter deals that existed at this point
            active_deals = [
                d for d in deals
                if d.created_date <= month_date.strftime("%Y-%m-%d")
            ]

            total = sum(d.usd_value for d in active_deals if d.stage not in (Stage.CLOSED_WON, Stage.CLOSED_LOST))
            weighted = sum(d.usd_value * d.probability for d in active_deals if d.stage not in (Stage.CLOSED_WON, Stage.CLOSED_LOST))
            won = sum(d.usd_value for d in active_deals if d.stage == Stage.CLOSED_WON and d.expected_close <= month_date.strftime("%Y-%m-%d"))
            new_deals = len([d for d in active_deals if d.created_date >= (month_date - timedelta(days=30)).strftime("%Y-%m-%d")])

            history.append({
                "month": month_str,
                "total_pipeline_usd": round(total, 2),
                "weighted_pipeline_usd": round(weighted, 2),
                "closed_won_usd": round(won, 2),
                "new_deals": new_deals,
                "active_deals": len(active_deals),
            })

        return history


if __name__ == "__main__":
    gen = DataGenerator()
    deals = gen.generate_full_pipeline()
    print(f"Generated {len(deals)} deals across {len(Entity)} entities")
    for entity in Entity:
        entity_deals = [d for d in deals if d.entity == entity]
        total_usd = sum(d.usd_value for d in entity_deals)
        print(f"  {entity.value}: {len(entity_deals)} deals, ${total_usd:,.0f} USD total")
