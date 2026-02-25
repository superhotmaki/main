#!/usr/bin/env python3
"""
APAC Pipeline Command Center - API Server
Serves consolidated pipeline data as JSON for the dashboard frontend.
Uses only Python standard library (http.server).
"""
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from engine import PipelineEngine
from models import Entity


# Pre-compute pipeline data on startup
print("Initializing pipeline engine...")
engine = PipelineEngine()
pipeline = engine.consolidate()
pipeline_data = pipeline.to_dict()
pipeline_json = json.dumps(pipeline_data)
print(f"Pipeline ready: {pipeline_data['total_deals']} deals, ${pipeline_data['total_pipeline_usd']:,.0f} USD")


class PipelineHandler(SimpleHTTPRequestHandler):
    """Handles API requests and serves static files."""

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/pipeline":
            self._json_response(pipeline_data)
        elif path == "/api/entities":
            self._json_response(pipeline_data["entities"])
        elif path.startswith("/api/entity/"):
            entity_code = path.split("/")[-1].upper()
            entity_data = next(
                (e for e in pipeline_data["entities"] if e["entity"] == entity_code),
                None
            )
            if entity_data:
                # Also include deals for this entity
                entity_deals = [d for d in pipeline_data["deals"] if d["entity"] == entity_code]
                entity_data_full = {**entity_data, "deals": entity_deals}
                self._json_response(entity_data_full)
            else:
                self._json_response({"error": f"Unknown entity: {entity_code}"}, 404)
        elif path == "/api/deals":
            params = parse_qs(parsed.query)
            deals = pipeline_data["deals"]
            # Filter by entity
            if "entity" in params:
                deals = [d for d in deals if d["entity"] == params["entity"][0].upper()]
            # Filter by stage
            if "stage" in params:
                deals = [d for d in deals if d["stage"] == params["stage"][0].upper()]
            # Filter by vertical
            if "vertical" in params:
                deals = [d for d in deals if d["vertical"] == params["vertical"][0].upper()]
            # Sort
            sort_by = params.get("sort", ["usd_value"])[0]
            reverse = params.get("order", ["desc"])[0] == "desc"
            if sort_by in deals[0] if deals else []:
                deals = sorted(deals, key=lambda d: d.get(sort_by, 0), reverse=reverse)
            self._json_response(deals)
        elif path == "/api/stages":
            self._json_response(pipeline_data["stage_summary"])
        elif path == "/api/verticals":
            self._json_response(pipeline_data["vertical_summary"])
        elif path == "/api/forecast":
            self._json_response(pipeline_data["forecast"])
        elif path == "/api/trends":
            self._json_response(pipeline_data["monthly_trend"])
        elif path == "/api/top":
            self._json_response(pipeline_data["top_deals"])
        elif path == "/api/risk":
            self._json_response(pipeline_data["at_risk_deals"])
        elif path == "/api/rates":
            self._json_response(pipeline_data["currency_rates"])
        elif path == "/api/search":
            params = parse_qs(parsed.query)
            term = params.get("q", [""])[0].lower()
            if not term:
                self._json_response({"error": "Missing search query parameter 'q'"}, 400)
                return
            results = [
                d for d in pipeline_data["deals"]
                if term in d["name"].lower()
                or term in d["owner"].lower()
                or term in d["entity_label"].lower()
                or term in d["vertical_label"].lower()
            ]
            self._json_response(results)
        elif path == "/" or path == "/index.html":
            self._serve_file("dashboard.html", "text/html")
        elif path.endswith(".html"):
            self._serve_file(path.lstrip("/"), "text/html")
        elif path.endswith(".js"):
            self._serve_file(path.lstrip("/"), "application/javascript")
        elif path.endswith(".css"):
            self._serve_file(path.lstrip("/"), "text/css")
        else:
            self._json_response({"error": "Not found"}, 404)

    def _json_response(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _serve_file(self, filename, content_type):
        filepath = os.path.join(os.path.dirname(__file__) or ".", filename)
        try:
            with open(filepath, "r") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")

    def log_message(self, format, *args):
        # Quieter logging
        if "/api/" in str(args[0]):
            return  # Don't log API calls
        super().log_message(format, *args)


def main():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), PipelineHandler)
    print(f"\nAPAC Pipeline Command Center running on http://localhost:{port}")
    print(f"Dashboard: http://localhost:{port}/")
    print(f"API: http://localhost:{port}/api/pipeline")
    print("Press Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
