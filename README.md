# Blood Test Report Analysis System

## Overview

This project aims to analyze blood test reports, find relevant health articles, and provide recommendations based on the analysis. We utilized Crew AI for task management and agent orchestration, implemented various tools for data processing, and used the Google Search API to find pertinent articles.

## Project Structure

The project is organized into several key components:

- **`agents.py`**: Defines the agents responsible for processing and analyzing data.
- **`tools.py`**: Contains the tools used for specific tasks such as parsing reports and searching for articles.
- **`tasks.py`**: Manages the high-level tasks that coordinate between agents and tools.
- **`search_tool.py`**: Handles interactions with the Google Search API to find relevant articles.

## Approach

### 1. Initial Setup

- **Environment Setup**:
  - Python was used as the primary programming language.
  - Crew AI was employed to manage tasks and agents.
  - PyMuPDF was used for converting PDF files to text.

- **Virtual Environment**:
  - A virtual environment (venv) was set up to manage dependencies.

### 2. Tool Development

- **`tools.py`**:
  - **`ReportParser`**: Parses PDF and text reports to extract relevant data.
  - **`SearchAPI`**: Interfaces with the Google Search API to find articles.
  - **`RecommendationEngine`**: Provides health recommendations based on the analysis.

- **Google Search API**:
  - Utilized the **SerperDevTool** to search for articles related to blood test results.
  - Modified search results by prepending `www.google.com` to URLs to ensure they are functional.

- **PyMuPDF Integration**:
  - **PDF to Text Conversion**: Converted PDF files to text format to facilitate easier data extraction and processing.

### 3. Agent and Task Management

- **`agents.py`**:
  - Defined agents for parsing reports, searching for articles, and generating recommendations.
  - **`ReportParserAgent`**: Handles report parsing and data extraction.
  - **`ArticleSearchAgent`**: Conducts web searches for articles based on extracted data.
  - **`RecommendationAgent`**: Generates health recommendations based on search results and analysis.

- **`tasks.py`**:
  - Manages tasks such as processing the blood test report, searching for articles, and providing recommendations.
  - Coordinates between different agents to complete the entire workflow.

### 4. How Crew AI is Used

- **Task Coordination**: Crew AI orchestrates the execution of various tasks, ensuring that each agent performs its role at the right time.
- **Agent Management**: Crew AI handles the communication between agents, allowing them to work together seamlessly.
- **Workflow Automation**: Automates the end-to-end process from report analysis to article search and recommendations.

### 5. Execution

- **Run the System**:
  - Start the system by executing `main.py`, which initiates the process.
  - The system reads a blood test report, analyzes it, searches for relevant articles, and provides health recommendations.

- **Sample Run**:
  - A sample blood test report is provided as input.
  - The report is parsed, and relevant health articles are searched for using the Google Search API.
  - Recommendations are generated based on the analysis and articles.

### 6. Version Control

- **Repository Cleanup**:
  - Removed the `venv` directory from version control and updated the `.gitignore` file.
  - Ensured that virtual environment files are not tracked by Git.

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/your-repository-url
```

2. **Install Dependencies:**
```
pip install -r requirements.txt
```

3. **Set Up Environment Variables:**
Create a .env file and add your Serper API key:
```
SERPER_API_KEY=your_api_key_here
```

4. **Run the System:**
```
python main.py
```

## Conclusion

This project demonstrates how to integrate Crew AI for task and agent management, leverage the Google Search API for finding relevant articles, and process PDF reports using PyMuPDF. By modularizing the code into agents, tools, and tasks, the system achieves a streamlined workflow for analyzing blood test reports and providing actionable health recommendations.
