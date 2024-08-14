# from crewai_tools import SerperDevTool
# import os
# from dotenv import load_dotenv
# import json

# # Load environment variables
# load_dotenv()

# # Initialize the tool with API key
# serper_api_key = os.getenv('SERPER_API_KEY')
# tool = SerperDevTool(api_key=serper_api_key)

# def perform_search(query):
#     search_results = tool.run(search_query=query)
#     results = []
#     # Assuming the response is a formatted string, process it
#     result_entries = search_results.split('---')
#     for result in result_entries:
#         if "Title:" in result:
#             title = result.split("Title:")[1].split("\n")[0].strip()
#             link = result.split("Link:")[1].split("\n")[0].strip()
#             snippet = result.split("Snippet:")[1].split("\n")[0].strip()
#             # Prepend 'https://www.google.com' to the link if not already present
#             if link.startswith('/'):
#                 link = 'https://www.google.com' + link
#             results.append({
#                 'title': title,
#                 'link': link,
#                 'snippet': snippet
#             })
#     return results

# if __name__ == "__main__":
#     query = "latest advancements in AI"
#     results = perform_search(query)
#     for result in results:
#         print(f"Title: {result['title']}")
#         print(f"Link: {result['link']}")
#         print(f"Snippet: {result['snippet']}")
#         print('---')
