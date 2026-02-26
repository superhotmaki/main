"""
Currency conversion engine for APAC Pipeline Command Center.
Uses realistic exchange rates for 8 APAC currencies to USD.
Supports historical rate simulation for trend analysis.
"""
from models import Currency
import random
from datetime import datetime, timedelta


# Base rates as of ~2024 (realistic approximations)
BASE_RATES_TO_USD = {
    Currency.AUD: 0.65,    # 1 AUD = 0.65 USD
    Currency.JPY: 0.0067,  # 1 JPY = 0.0067 USD
    Currency.SGD: 0.74,    # 1 SGD = 0.74 USD
    Currency.HKD: 0.128,   # 1 HKD = 0.128 USD
    Currency.KRW: 0.00075, # 1 KRW = 0.00075 USD
    Currency.INR: 0.012,   # 1 INR = 0.012 USD
    Currency.THB: 0.028,   # 1 THB = 0.028 USD
    Currency.IDR: 0.000063,# 1 IDR = 0.000063 USD
    Currency.USD: 1.0,
}

# Volatility per currency (annualized %)
VOLATILITY = {
    Currency.AUD: 0.08,
    Currency.JPY: 0.10,
    Currency.SGD: 0.04,
    Currency.HKD: 0.01,
    Currency.KRW: 0.09,
    Currency.INR: 0.06,
    Currency.THB: 0.07,
    Currency.IDR: 0.08,
    Currency.USD: 0.0,
}


class CurrencyEngine:
    """Handles all currency conversions with simulated rate fluctuation."""

    def __init__(self, base_rates=None, seed=42):
        self.base_rates = base_rates or dict(BASE_RATES_TO_USD)
        self.rng = random.Random(seed)
        self._rate_cache = {}

    def get_rate(self, currency: Currency, as_of_date: str = None) -> float:
        """Get exchange rate to USD for a given currency and date."""
        if currency == Currency.USD:
            return 1.0

        if as_of_date is None:
            return self.base_rates[currency]

        cache_key = (currency, as_of_date)
        if cache_key in self._rate_cache:
            return self._rate_cache[cache_key]

        # Simulate rate fluctuation based on date
        base = self.base_rates[currency]
        vol = VOLATILITY[currency]

        # Use date hash for deterministic but varied rates
        date_hash = hash(as_of_date + currency.value)
        self.rng.seed(date_hash)
        fluctuation = self.rng.gauss(0, vol / 12)  # Monthly vol
        rate = base * (1 + fluctuation)

        self._rate_cache[cache_key] = rate
        return rate

    def convert_to_usd(self, amount: float, currency: Currency, as_of_date: str = None) -> float:
        """Convert a local currency amount to USD."""
        rate = self.get_rate(currency, as_of_date)
        return amount * rate

    def convert_from_usd(self, usd_amount: float, currency: Currency, as_of_date: str = None) -> float:
        """Convert USD to a local currency."""
        rate = self.get_rate(currency, as_of_date)
        if rate == 0:
            return 0
        return usd_amount / rate

    def get_all_rates(self, as_of_date: str = None) -> dict:
        """Get all exchange rates as a dict."""
        rates = {}
        for curr in Currency:
            rate = self.get_rate(curr, as_of_date)
            rates[curr.value] = round(rate, 6)
        return rates

    def get_rate_history(self, currency: Currency, months: int = 12) -> list:
        """Get simulated rate history for a currency over N months."""
        history = []
        today = datetime.now()
        for i in range(months, -1, -1):
            dt = today - timedelta(days=i * 30)
            date_str = dt.strftime("%Y-%m-%d")
            rate = self.get_rate(currency, date_str)
            history.append({
                "date": date_str,
                "rate": round(rate, 6),
            })
        return history

    def format_currency(self, amount: float, currency: Currency) -> str:
        """Format an amount in its local currency display."""
        symbols = {
            Currency.AUD: "A$",
            Currency.JPY: "¥",
            Currency.SGD: "S$",
            Currency.HKD: "HK$",
            Currency.KRW: "₩",
            Currency.INR: "₹",
            Currency.THB: "฿",
            Currency.IDR: "Rp",
            Currency.USD: "$",
        }
        symbol = symbols.get(currency, "$")

        if currency in (Currency.JPY, Currency.KRW, Currency.IDR):
            return f"{symbol}{amount:,.0f}"
        return f"{symbol}{amount:,.2f}"


# Module-level convenience instance
engine = CurrencyEngine()


def to_usd(amount: float, currency: Currency, as_of_date: str = None) -> float:
    return engine.convert_to_usd(amount, currency, as_of_date)


def from_usd(usd_amount: float, currency: Currency, as_of_date: str = None) -> float:
    return engine.convert_from_usd(usd_amount, currency, as_of_date)


def rates(as_of_date: str = None) -> dict:
    return engine.get_all_rates(as_of_date)
