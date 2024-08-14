# tasks.py

from tools import HealthAnalyzer

def run_health_analysis(report_path):
    analyzer = HealthAnalyzer()
    analysis = analyzer.analyze_report(report_path)
    query = "health issues related to blood test findings"
    articles = analyzer.find_articles(query)
    recommendations = analyzer.generate_recommendations(analysis)
    return analysis, articles, recommendations
