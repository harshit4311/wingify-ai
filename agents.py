# agents.py

class ReportParser:
    def parse(self, report_path):
        if report_path.lower().endswith('.pdf'):
            return self.parse_pdf(report_path)
        else:
            return self.parse_text(report_path)

    def parse_pdf(self, pdf_path):
        import fitz  # PyMuPDF library
        text = ''
        with fitz.open(pdf_path) as pdf:
            for page_num in range(len(pdf)):
                page = pdf.load_page(page_num)
                text += page.get_text()
        data = self.extract_data(text)
        return data

    def parse_text(self, text_path):
        with open(text_path, 'r') as file:
            text = file.read()
        data = self.extract_data(text)
        return data

    def extract_data(self, text):
        return {
            'glucose_level': 'Normal',
            'cholesterol_level': 'High',
        }

class SearchAPI:
    def search(self, query):
        import requests
        from bs4 import BeautifulSoup
        
        search_url = f"https://www.google.com/search?q={query}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = self.extract_articles(soup)
        return articles

    def extract_articles(self, soup):
        articles = []
        for result in soup.find_all('a', href=True):
            link = result['href']
            if link.startswith('/'):
                link = 'https://www.google.com' + link
            articles.append({
                'title': result.text,
                'url': link
            })
        return articles

class RecommendationEngine:
    def generate(self, analysis, articles):
        recommendations = []

        if 'High' in analysis.get('cholesterol_level', ''):
            recommendations.append("Consider reducing saturated fat intake.")
            recommendations.append("Increase your intake of soluble fiber.")
            recommendations.append("Exercise regularly to help lower cholesterol levels.")
            recommendations.append("Limit your intake of red meat and full-fat dairy products.")
            recommendations.append("Incorporate more omega-3 fatty acids into your diet.")
            recommendations.append("")

        if 'Normal' in analysis.get('glucose_level', ''):
            recommendations.append("Maintain your current diet to keep glucose levels stable.")
            recommendations.append("Continue regular physical activity.")
            recommendations.append("Monitor blood sugar levels periodically.")
            recommendations.append("")

        if 'Low' in analysis.get('glucose_level', ''):
            recommendations.append("Increase carbohydrate intake to stabilize glucose levels.")
            recommendations.append("Consider eating smaller, more frequent meals.")
            recommendations.append("Avoid skipping meals, especially breakfast.")
            recommendations.append("")

        if 'Elevated' in analysis.get('blood_pressure', ''):
            recommendations.append("Reduce salt intake to help manage blood pressure.")
            recommendations.append("Avoid processed foods that are high in sodium.")
            recommendations.append("Engage in regular cardiovascular exercise.")
            recommendations.append("Monitor your blood pressure regularly.")
            recommendations.append("")

        # Additional generic recommendations
        recommendations.append("Stay hydrated by drinking enough water and taking electrolytes throughout the day.")
        recommendations.append("Make sure you go out in the sun evry morning and get that daily dose of Vitamin-D.")
        recommendations.append("Avoid smoking and alcohol consumption.")
        recommendations.append("Ensure you get sufficient sleep every night.")
        recommendations.append("Manage stress through relaxation techniques like meditation or yoga.")
        # recommendations.append("")

        return recommendations
