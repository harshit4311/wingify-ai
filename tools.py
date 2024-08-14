# tools.py

from agents import ReportParser, SearchAPI, RecommendationEngine

class HealthAnalyzer:
    def __init__(self):
        self.report_parser = ReportParser()
        self.search_api = SearchAPI()
        self.recommendation_engine = RecommendationEngine()

    def analyze_report(self, report_path):
        return self.report_parser.parse(report_path)

    def find_articles(self, query):
        return self.search_api.search(query)

    def generate_recommendations(self, analysis):
        return self.recommendation_engine.generate(analysis, [])
