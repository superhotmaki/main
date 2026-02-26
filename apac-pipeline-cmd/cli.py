#!/usr/bin/env python3
"""
APAC Pipeline Command Center - CLI Tool
A fast, terminal-native interface for querying consolidated pipeline data.

Usage:
    python cli.py overview
    python cli.py entity AU
    python cli.py top [N]
    python cli.py risk
    python cli.py forecast
    python cli.py stage
    python cli.py vertical
    python cli.py search <term>
    python cli.py rates
    python cli.py export [filename]
"""
import sys
import json
from engine import PipelineEngine
from models import Entity, Stage, Currency


# Terminal colors
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_GREEN = "\033[42m"
    BG_RED = "\033[41m"


def fmt_usd(val):
    """Format USD value with color based on magnitude."""
    if val >= 1_000_000:
        return f"{C.GREEN}${val:>12,.0f}{C.RESET}"
    elif val >= 100_000:
        return f"{C.CYAN}${val:>12,.0f}{C.RESET}"
    else:
        return f"${val:>12,.0f}"


def fmt_pct(val):
    """Format percentage with color."""
    pct = val * 100
    if pct >= 60:
        return f"{C.GREEN}{pct:>5.1f}%{C.RESET}"
    elif pct >= 30:
        return f"{C.YELLOW}{pct:>5.1f}%{C.RESET}"
    else:
        return f"{C.RED}{pct:>5.1f}%{C.RESET}"


def bar(value, max_value, width=30, char="█"):
    """Create a simple bar chart."""
    if max_value == 0:
        return ""
    filled = int(value / max_value * width)
    return f"{C.CYAN}{char * filled}{C.DIM}{'░' * (width - filled)}{C.RESET}"


def header(text):
    print(f"\n{C.BOLD}{C.BG_BLUE} {text} {C.RESET}\n")


def subheader(text):
    print(f"  {C.BOLD}{C.YELLOW}{text}{C.RESET}")


def divider():
    print(f"  {C.DIM}{'─' * 70}{C.RESET}")


def cmd_overview(pipeline):
    """Show high-level pipeline overview."""
    p = pipeline.to_dict()

    header("APAC PIPELINE COMMAND CENTER")
    print(f"  {C.DIM}Generated: {p['generated_at']} | Reporting Currency: USD{C.RESET}")
    print()

    # Key metrics
    subheader("KEY METRICS")
    print(f"  Total Deals:       {C.BOLD}{p['total_deals']}{C.RESET}")
    print(f"  Total Pipeline:    {fmt_usd(p['total_pipeline_usd'])}")
    print(f"  Weighted Pipeline: {fmt_usd(p['weighted_pipeline_usd'])}")
    print(f"  At-Risk Deals:     {C.RED if len(p['at_risk_deals']) > 10 else C.YELLOW}{len(p['at_risk_deals'])}{C.RESET}")
    print()

    # Entity table
    subheader("ENTITY BREAKDOWN")
    print(f"  {C.DIM}{'Entity':<15} {'Deals':>6} {'Pipeline USD':>14} {'Weighted':>14} {'Win Rate':>8} {'Velocity':>10}{C.RESET}")
    divider()

    max_pipeline = max(e['total_usd_value'] for e in p['entities'])
    for e in sorted(p['entities'], key=lambda x: x['total_usd_value'], reverse=True):
        print(
            f"  {e['entity_label']:<15}"
            f" {e['total_deals']:>5} "
            f" {fmt_usd(e['total_usd_value'])}"
            f" {fmt_usd(e['weighted_pipeline'])}"
            f" {fmt_pct(e['conversion_rate'])}"
            f" {e['velocity_days']:>7.0f}d"
        )
        print(f"  {'':>15} {bar(e['total_usd_value'], max_pipeline)}")
    print()

    # Forecast
    subheader("3-MONTH FORECAST")
    for month, data in p['forecast'].items():
        print(f"  {month}: {data['deals']} deals | Total: {fmt_usd(data['total_usd'])} | Weighted: {fmt_usd(data['weighted_usd'])}")
    print()


def cmd_entity(pipeline, entity_code):
    """Show detailed view for a single entity."""
    try:
        entity = Entity[entity_code.upper()]
    except KeyError:
        print(f"{C.RED}Unknown entity: {entity_code}{C.RESET}")
        print(f"Valid entities: {', '.join(e.name for e in Entity)}")
        return

    p = pipeline.to_dict()
    entity_data = next((e for e in p['entities'] if e['entity'] == entity_code.upper()), None)
    if not entity_data:
        print(f"{C.RED}No data for {entity_code}{C.RESET}")
        return

    e = entity_data
    header(f"ENTITY: {e['entity_label']} ({e['entity']})")
    print(f"  {C.DIM}Local Currency: {e['currency']}{C.RESET}")
    print()

    subheader("SUMMARY")
    print(f"  Total Deals:       {C.BOLD}{e['total_deals']}{C.RESET}")
    print(f"  Local Value:       {e['total_local_value']:>14,.0f} {e['currency']}")
    print(f"  USD Value:         {fmt_usd(e['total_usd_value'])}")
    print(f"  Weighted:          {fmt_usd(e['weighted_pipeline'])}")
    print(f"  Avg Deal Size:     {fmt_usd(e['avg_deal_size_usd'])}")
    print(f"  Largest Deal:      {fmt_usd(e['largest_deal_usd'])}")
    print(f"  Win Rate:          {fmt_pct(e['conversion_rate'])}")
    print(f"  Avg Velocity:      {e['velocity_days']:.0f} days")
    print()

    subheader("STAGE BREAKDOWN")
    for stage_name, stage_data in e['deals_by_stage'].items():
        count = stage_data['count']
        total = stage_data['total_usd']
        pct_of_total = total / e['total_usd_value'] if e['total_usd_value'] > 0 else 0
        print(f"  {stage_name:<14} {count:>3} deals  {fmt_usd(total)}  {bar(total, e['total_usd_value'], width=20)}")
    print()

    # Top deals for this entity
    entity_deals = [d for d in p['deals'] if d['entity'] == entity_code.upper()]
    top = sorted(entity_deals, key=lambda d: d['usd_value'], reverse=True)[:5]
    subheader("TOP 5 DEALS")
    for d in top:
        stage_color = C.GREEN if d['stage'] == 'CLOSED_WON' else C.RED if d['stage'] == 'CLOSED_LOST' else C.CYAN
        print(f"  {stage_color}{d['stage_label']:<14}{C.RESET} {fmt_usd(d['usd_value'])}  {d['name'][:45]}")
    print()


def cmd_top(pipeline, n=10):
    """Show top N deals across all entities."""
    p = pipeline.to_dict()
    header(f"TOP {n} DEALS")
    print(f"  {C.DIM}{'#':>3} {'Entity':>4} {'Stage':<14} {'USD Value':>14} {'Prob':>6} {'Weighted':>12} {'Name'}{C.RESET}")
    divider()

    for i, d in enumerate(p['top_deals'][:n], 1):
        stage_color = C.GREEN if d['stage'] == 'CLOSED_WON' else C.YELLOW if d['stage'] == 'NEGOTIATION' else C.CYAN
        print(
            f"  {i:>3}"
            f" {d['entity']:>4}"
            f" {stage_color}{d['stage_label']:<14}{C.RESET}"
            f" {fmt_usd(d['usd_value'])}"
            f" {fmt_pct(d['probability'])}"
            f" {fmt_usd(d['weighted_value'])}"
            f"  {d['name'][:35]}"
        )
    print()


def cmd_risk(pipeline):
    """Show at-risk deals (stale 30+ days)."""
    p = pipeline.to_dict()
    at_risk = p['at_risk_deals']

    header(f"AT-RISK DEALS ({len(at_risk)} deals, no activity 30+ days)")

    if not at_risk:
        print(f"  {C.GREEN}No at-risk deals! All deals have recent activity.{C.RESET}")
        return

    total_at_risk = sum(d['usd_value'] for d in at_risk)
    print(f"  {C.RED}Total at-risk value: ${total_at_risk:,.0f} USD{C.RESET}")
    print()

    print(f"  {C.DIM}{'Entity':>4} {'Stage':<14} {'USD Value':>14} {'Last Activity':>14} {'Name'}{C.RESET}")
    divider()

    for d in at_risk[:20]:
        print(
            f"  {d['entity']:>4}"
            f" {C.YELLOW}{d['stage_label']:<14}{C.RESET}"
            f" {fmt_usd(d['usd_value'])}"
            f" {C.RED}{d['last_activity']:>14}{C.RESET}"
            f"  {d['name'][:40]}"
        )
    if len(at_risk) > 20:
        print(f"\n  {C.DIM}... and {len(at_risk) - 20} more{C.RESET}")
    print()


def cmd_forecast(pipeline):
    """Show 3-month forecast with entity breakdown."""
    p = pipeline.to_dict()
    header("3-MONTH PIPELINE FORECAST")

    for month, data in p['forecast'].items():
        subheader(f"{month}")
        print(f"  Deals:    {data['deals']}")
        print(f"  Total:    {fmt_usd(data['total_usd'])}")
        print(f"  Weighted: {fmt_usd(data['weighted_usd'])}")

        if data['by_entity']:
            max_val = max(e['total_usd'] for e in data['by_entity'].values())
            for ename, edata in sorted(data['by_entity'].items(), key=lambda x: x[1]['total_usd'], reverse=True):
                print(f"    {ename:>4}: {edata['deals']:>2} deals {fmt_usd(edata['total_usd'])} {bar(edata['total_usd'], max_val, width=15)}")
        print()


def cmd_stage(pipeline):
    """Show pipeline by stage."""
    p = pipeline.to_dict()
    header("PIPELINE BY STAGE")

    print(f"  {C.DIM}{'Stage':<14} {'Count':>6} {'Total USD':>14} {'Weighted USD':>14} {'Avg Deal':>12}{C.RESET}")
    divider()

    max_total = max(s['total_usd'] for s in p['stage_summary'].values())
    for stage_name, data in p['stage_summary'].items():
        print(
            f"  {stage_name:<14}"
            f" {data['count']:>5} "
            f" {fmt_usd(data['total_usd'])}"
            f" {fmt_usd(data['weighted_usd'])}"
            f" {fmt_usd(data['avg_deal_size'])}"
        )
        print(f"  {'':>14} {bar(data['total_usd'], max_total)}")
    print()


def cmd_vertical(pipeline):
    """Show pipeline by vertical."""
    p = pipeline.to_dict()
    header("PIPELINE BY VERTICAL")

    print(f"  {C.DIM}{'Vertical':<16} {'Count':>6} {'Total USD':>14} {'Weighted USD':>14}{C.RESET}")
    divider()

    max_total = max(v['total_usd'] for v in p['vertical_summary'].values()) if p['vertical_summary'] else 1
    for vert_name, data in sorted(p['vertical_summary'].items(), key=lambda x: x[1]['total_usd'], reverse=True):
        print(
            f"  {vert_name:<16}"
            f" {data['count']:>5} "
            f" {fmt_usd(data['total_usd'])}"
            f" {fmt_usd(data['weighted_usd'])}"
        )
        print(f"  {'':>16} {bar(data['total_usd'], max_total, width=25)}")
        # Entity breakdown
        for ename, edata in sorted(data['entities'].items(), key=lambda x: x[1]['total_usd'], reverse=True)[:3]:
            print(f"  {'':>16} {C.DIM}{ename}: {edata['count']} deals, ${edata['total_usd']:,.0f}{C.RESET}")
    print()


def cmd_search(pipeline, term):
    """Search deals by name, owner, or entity."""
    p = pipeline.to_dict()
    term_lower = term.lower()

    results = [
        d for d in p['deals']
        if term_lower in d['name'].lower()
        or term_lower in d['owner'].lower()
        or term_lower in d['entity'].lower()
        or term_lower in d['entity_label'].lower()
        or term_lower in d['vertical_label'].lower()
    ]

    header(f"SEARCH: '{term}' ({len(results)} results)")

    if not results:
        print(f"  No deals found matching '{term}'")
        return

    print(f"  {C.DIM}{'Entity':>4} {'Stage':<14} {'USD Value':>14} {'Owner':<20} {'Name'}{C.RESET}")
    divider()

    for d in sorted(results, key=lambda x: x['usd_value'], reverse=True)[:25]:
        print(
            f"  {d['entity']:>4}"
            f" {d['stage_label']:<14}"
            f" {fmt_usd(d['usd_value'])}"
            f" {d['owner']:<20}"
            f" {d['name'][:35]}"
        )
    if len(results) > 25:
        print(f"\n  {C.DIM}... and {len(results) - 25} more{C.RESET}")
    print()


def cmd_rates(pipeline):
    """Show current exchange rates."""
    p = pipeline.to_dict()
    header("EXCHANGE RATES (to USD)")

    for curr, rate in sorted(p['currency_rates'].items()):
        if curr == "USD":
            continue
        inverse = 1.0 / rate if rate > 0 else 0
        print(f"  1 {curr} = ${rate:.6f} USD  |  $1 USD = {inverse:,.2f} {curr}")
    print()


def cmd_export(pipeline, filename="pipeline_data.json"):
    """Export full consolidated data as JSON."""
    data = pipeline.to_json()
    with open(filename, 'w') as f:
        f.write(data)
    print(f"{C.GREEN}Exported to {filename} ({len(data):,} bytes){C.RESET}")


def cmd_help():
    """Show help."""
    header("APAC PIPELINE COMMAND CENTER - CLI")
    print("""  Usage: python cli.py <command> [args]

  Commands:
    overview           High-level pipeline summary across all entities
    entity <code>      Detailed view for one entity (AU, JP, SG, HK, KR, IN, TH, ID)
    top [N]            Top N deals by value (default: 10)
    risk               Deals with no activity in 30+ days
    forecast           3-month pipeline forecast
    stage              Pipeline breakdown by stage
    vertical           Pipeline breakdown by vertical
    search <term>      Search deals by name, owner, entity, or vertical
    rates              Current exchange rates
    export [file]      Export consolidated data as JSON
    help               This help message
""")


def main():
    if len(sys.argv) < 2:
        cmd_help()
        return

    # Initialize engine (data generation happens here)
    engine = PipelineEngine()
    pipeline = engine.consolidate()

    cmd = sys.argv[1].lower()

    if cmd == "overview":
        cmd_overview(pipeline)
    elif cmd == "entity":
        if len(sys.argv) < 3:
            print(f"{C.RED}Usage: python cli.py entity <code>{C.RESET}")
            print(f"Codes: {', '.join(e.name for e in Entity)}")
        else:
            cmd_entity(pipeline, sys.argv[2])
    elif cmd == "top":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        cmd_top(pipeline, n)
    elif cmd == "risk":
        cmd_risk(pipeline)
    elif cmd == "forecast":
        cmd_forecast(pipeline)
    elif cmd == "stage":
        cmd_stage(pipeline)
    elif cmd == "vertical":
        cmd_vertical(pipeline)
    elif cmd == "search":
        if len(sys.argv) < 3:
            print(f"{C.RED}Usage: python cli.py search <term>{C.RESET}")
        else:
            cmd_search(pipeline, " ".join(sys.argv[2:]))
    elif cmd == "rates":
        cmd_rates(pipeline)
    elif cmd == "export":
        filename = sys.argv[2] if len(sys.argv) > 2 else "pipeline_data.json"
        cmd_export(pipeline, filename)
    elif cmd == "help":
        cmd_help()
    else:
        print(f"{C.RED}Unknown command: {cmd}{C.RESET}")
        cmd_help()


if __name__ == "__main__":
    main()
