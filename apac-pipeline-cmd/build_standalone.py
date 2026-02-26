#!/usr/bin/env python3
"""
Builds a standalone dashboard HTML file with embedded data.
No server needed - just open the HTML file directly in a browser.
"""
from engine import PipelineEngine
import json
import re


def build():
    print("Generating pipeline data...")
    engine = PipelineEngine()
    pipeline = engine.consolidate()
    data_json = pipeline.to_json()
    print(f"  {pipeline.total_deals} deals, ${pipeline.total_pipeline_usd:,.0f} USD")

    print("Reading dashboard template...")
    with open("dashboard.html", "r") as f:
        html = f.read()

    # Replace the fetch-based data loading with inline data
    inline_script = f"""
async function loadData() {{
  DATA = {data_json};
  document.getElementById('loading').style.display = 'none';
  renderAll();
}}
"""

    # Find and replace the loadData function
    pattern = r'async function loadData\(\) \{.*?\n\}'
    html = re.sub(pattern, inline_script.strip(), html, flags=re.DOTALL)

    output_file = "dashboard-standalone.html"
    with open(output_file, "w") as f:
        f.write(html)

    size_kb = len(html) / 1024
    print(f"Built {output_file} ({size_kb:.0f} KB)")
    print(f"Open in browser: file://{output_file}")


if __name__ == "__main__":
    build()
