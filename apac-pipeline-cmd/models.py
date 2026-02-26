"""
Data models for APAC Pipeline Command Center.
Represents entities, deals, currencies, and pipeline stages across 8 APAC markets.
"""
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional
from datetime import datetime, date
import json


class Entity(Enum):
    """8 APAC business entities."""
    AU = "Australia"
    JP = "Japan"
    SG = "Singapore"
    HK = "Hong Kong"
    KR = "South Korea"
    IN = "India"
    TH = "Thailand"
    ID = "Indonesia"


class Currency(Enum):
    """Local currencies for each entity."""
    AUD = "AUD"
    JPY = "JPY"
    SGD = "SGD"
    HKD = "HKD"
    KRW = "KRW"
    INR = "INR"
    THB = "THB"
    IDR = "IDR"
    USD = "USD"  # Consolidated reporting currency


# Entity to local currency mapping
ENTITY_CURRENCY = {
    Entity.AU: Currency.AUD,
    Entity.JP: Currency.JPY,
    Entity.SG: Currency.SGD,
    Entity.HK: Currency.HKD,
    Entity.KR: Currency.KRW,
    Entity.IN: Currency.INR,
    Entity.TH: Currency.THB,
    Entity.ID: Currency.IDR,
}


class Stage(Enum):
    """Pipeline stages in order."""
    PROSPECT = "Prospect"
    QUALIFIED = "Qualified"
    PROPOSAL = "Proposal"
    NEGOTIATION = "Negotiation"
    CLOSED_WON = "Closed Won"
    CLOSED_LOST = "Closed Lost"


# Stage progression weights for forecasting
STAGE_WEIGHTS = {
    Stage.PROSPECT: 0.10,
    Stage.QUALIFIED: 0.25,
    Stage.PROPOSAL: 0.50,
    Stage.NEGOTIATION: 0.75,
    Stage.CLOSED_WON: 1.00,
    Stage.CLOSED_LOST: 0.00,
}


class DealSize(Enum):
    """Deal size categories."""
    SMALL = "Small"       # < $50K USD
    MEDIUM = "Medium"     # $50K - $250K USD
    LARGE = "Large"       # $250K - $1M USD
    ENTERPRISE = "Enterprise"  # > $1M USD


class Vertical(Enum):
    """Industry verticals."""
    FINTECH = "Fintech"
    ECOMMERCE = "E-Commerce"
    SAAS = "SaaS"
    MANUFACTURING = "Manufacturing"
    LOGISTICS = "Logistics"
    HEALTHCARE = "Healthcare"
    GOVERNMENT = "Government"


@dataclass
class Deal:
    """A single deal in the pipeline."""
    id: str
    name: str
    entity: Entity
    currency: Currency
    local_value: float
    usd_value: float
    stage: Stage
    vertical: Vertical
    owner: str
    created_date: str
    expected_close: str
    last_activity: str
    probability: float  # 0-1
    notes: str = ""

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "entity": self.entity.name,
            "entity_label": self.entity.value,
            "currency": self.currency.value,
            "local_value": self.local_value,
            "usd_value": round(self.usd_value, 2),
            "stage": self.stage.name,
            "stage_label": self.stage.value,
            "vertical": self.vertical.name,
            "vertical_label": self.vertical.value,
            "owner": self.owner,
            "created_date": self.created_date,
            "expected_close": self.expected_close,
            "last_activity": self.last_activity,
            "probability": self.probability,
            "weighted_value": round(self.usd_value * self.probability, 2),
            "notes": self.notes,
        }


@dataclass
class EntitySummary:
    """Aggregated summary for a single entity."""
    entity: Entity
    currency: Currency
    total_deals: int
    total_local_value: float
    total_usd_value: float
    weighted_pipeline: float
    deals_by_stage: dict
    avg_deal_size_usd: float
    largest_deal_usd: float
    conversion_rate: float  # won / (won + lost)
    velocity_days: float  # avg days from prospect to close

    def to_dict(self):
        return {
            "entity": self.entity.name,
            "entity_label": self.entity.value,
            "currency": self.currency.value,
            "total_deals": self.total_deals,
            "total_local_value": round(self.total_local_value, 2),
            "total_usd_value": round(self.total_usd_value, 2),
            "weighted_pipeline": round(self.weighted_pipeline, 2),
            "deals_by_stage": self.deals_by_stage,
            "avg_deal_size_usd": round(self.avg_deal_size_usd, 2),
            "largest_deal_usd": round(self.largest_deal_usd, 2),
            "conversion_rate": round(self.conversion_rate, 4),
            "velocity_days": round(self.velocity_days, 1),
        }


@dataclass
class ConsolidatedPipeline:
    """Full consolidated view across all entities."""
    generated_at: str
    reporting_currency: str
    total_deals: int
    total_pipeline_usd: float
    weighted_pipeline_usd: float
    entities: list  # List of EntitySummary dicts
    deals: list     # List of Deal dicts
    stage_summary: dict
    vertical_summary: dict
    currency_rates: dict
    monthly_trend: list
    top_deals: list
    at_risk_deals: list  # Deals with no activity in 30+ days
    forecast: dict

    def to_dict(self):
        return {
            "generated_at": self.generated_at,
            "reporting_currency": self.reporting_currency,
            "total_deals": self.total_deals,
            "total_pipeline_usd": round(self.total_pipeline_usd, 2),
            "weighted_pipeline_usd": round(self.weighted_pipeline_usd, 2),
            "entities": self.entities,
            "deals": self.deals,
            "stage_summary": self.stage_summary,
            "vertical_summary": self.vertical_summary,
            "currency_rates": self.currency_rates,
            "monthly_trend": self.monthly_trend,
            "top_deals": self.top_deals,
            "at_risk_deals": self.at_risk_deals,
            "forecast": self.forecast,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)
