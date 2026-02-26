# APAC Pipeline Command Center

A consolidated cross-border pipeline management tool that takes messy multi-entity, multi-currency deal data across 8 APAC markets (Australia, Japan, Singapore, Hong Kong, South Korea, India, Thailand, Indonesia) and renders it into one clear, queryable picture. Includes a terminal CLI for fast queries, a REST API, and a real-time interactive dashboard — all built with zero external dependencies.

## What It Does

- **Consolidates** pipeline data across 8 APAC entities with 8 different local currencies into a single USD-normalized view
- **210 synthetic deals** with realistic company names, deal values in local currencies, stage progression, verticals, owners, and activity timestamps
- **Currency engine** with real-world exchange rates for AUD, JPY, SGD, HKD, KRW, INR, THB, IDR
- **Pipeline analytics**: stage funnels, vertical breakdowns, entity comparisons, win rates, deal velocity, weighted forecasts
- **At-risk detection**: flags deals with no activity in 30+ days
- **3-month forecast** broken down by entity
- **Entity × Vertical heat map** for spotting concentration risk

## How to Run

### Prerequisites
- Python 3.8+ (no external packages needed — everything uses the standard library)

### CLI (instant, no server needed)
```bash
cd apac-pipeline-cmd

# Overview of entire APAC pipeline
python cli.py overview

# Deep dive into one entity
python cli.py entity JP

# Top deals by value
python cli.py top 15

# At-risk deals (stale 30+ days)
python cli.py risk

# 3-month forecast
python cli.py forecast

# Pipeline by stage
python cli.py stage

# Pipeline by vertical
python cli.py vertical

# Search across everything
python cli.py search "cloud"
python cli.py search "fintech"

# Exchange rates
python cli.py rates

# Export full dataset as JSON
python cli.py export pipeline_data.json

# Help
python cli.py help
```

### Dashboard (interactive web UI)

**Option A: Standalone (no server needed)**
```bash
python build_standalone.py
# Open dashboard-standalone.html in your browser
```

**Option B: With live API server**
```bash
python server.py
# Open http://localhost:8080 in your browser
```

The dashboard includes:
- Overview with key metrics, entity bars, stage donut, trend sparklines
- Clickable entity cards with drill-down detail views
- Pipeline funnel with entity × stage matrix
- Vertical breakdown with entity cross-tabulation
- Full deal table with search, sort, and stage filters
- 3-month forecast with entity breakdown
- At-risk deal tracker with staleness indicators
- Currency rates and impact analysis

### API Endpoints
```
GET /api/pipeline     Full consolidated data
GET /api/entities     All entity summaries
GET /api/entity/AU    Single entity detail (AU, JP, SG, HK, KR, IN, TH, ID)
GET /api/deals        All deals (filterable: ?entity=AU&stage=PROSPECT&vertical=FINTECH)
GET /api/stages       Pipeline by stage
GET /api/verticals    Pipeline by vertical
GET /api/forecast     3-month forecast
GET /api/trends       Monthly pipeline trend
GET /api/top          Top deals
GET /api/risk         At-risk deals
GET /api/rates        Exchange rates
GET /api/search?q=    Search deals
```

## What I'd Need to Change to Make It Real

1. **Real data source**: Replace `datagen.py` with connectors to your actual CRM (Salesforce, HubSpot, Pipedrive, etc.) or database. The `Deal` dataclass is the interface — anything that produces `Deal` objects plugs in.

2. **Live exchange rates**: Replace the static rates in `currency.py` with an API call to a rates provider (e.g., Open Exchange Rates, XE, or your treasury system). The `CurrencyEngine` class already supports date-based lookups.

3. **Authentication**: The server has no auth. Add API key middleware or integrate with your SSO for the dashboard.

4. **Persistence**: Currently regenerates data on every run. Add SQLite or PostgreSQL for deal storage, historical snapshots, and audit trails.

5. **Real-time updates**: Add WebSocket support for live deal updates pushing to the dashboard.

6. **Entity-specific business rules**: Different APAC markets have different fiscal years, reporting requirements, and deal stage definitions. The model supports this but it's not implemented.

## Architecture

```
models.py              Data models (Entity, Currency, Stage, Deal, etc.)
currency.py            Currency conversion engine with 8 APAC currencies
datagen.py             Synthetic data generator (210 realistic deals)
engine.py              Pipeline consolidation engine (aggregation, forecasting, risk)
cli.py                 Terminal CLI with 10 commands
server.py              HTTP API server (Python stdlib, no dependencies)
dashboard.html         Interactive dashboard (fetches from API)
build_standalone.py    Builds a standalone dashboard with embedded data
dashboard-standalone.html  Self-contained dashboard (no server needed)
```

## Known Limitations

- Data is synthetic (but realistic in structure, scale, and distribution)
- Exchange rates are static snapshots, not live
- No authentication on the API
- Dashboard is read-only (no deal editing)
- Trend data is simulated backward from current state, not from actual historical snapshots
- The "velocity" metric is based on creation-to-close dates, not stage transition timestamps
- No data persistence between runs

## Stack

- **Backend**: Python 3 standard library only (no pip install needed)
- **Frontend**: Single-file HTML with vanilla JS and CSS (no build step, no React, no npm)
- **Server**: Python `http.server` module
- **Data**: Generated in-memory with deterministic seeding for reproducibility
