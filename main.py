# main.py

from tasks import run_health_analysis

if __name__ == "__main__":
    report_path = '/Users/harshit/Programming/Web Development/wingify-ai/BloodTest-Report.pdf'  # Adjust path as necessary
    analysis, articles, recommendations = run_health_analysis(report_path)

    print("Analysis:")
    print(analysis)
    
    print("\nRecommendations:")
    for rec in recommendations:
        print(f"- {rec}")

    print("\nArticles:")
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print('---')
