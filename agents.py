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
        return recommendations
