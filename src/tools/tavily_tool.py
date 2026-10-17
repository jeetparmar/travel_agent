import os
import logging
from dotenv import load_dotenv
from tavily import TavilyClient
from ..constants import TAVILY_MAX_RESULTS, TAVILY_SNIPPET_LENGTH

logger = logging.getLogger(__name__)

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY environment variable is not set")



client = TavilyClient(api_key=TAVILY_API_KEY)


def tavily_search(query):
    logger.info(f"Tavily tool: Searching for {query}")
    try:
        response = client.search(query=query, max_results=TAVILY_MAX_RESULTS)
        results = []
        for i, r in enumerate(response.get("results", []), 1):
            title = r.get("title", "unknown")
            url = r.get("url", "")
            snippet = r.get("content", "").strip()
            if len(snippet) > TAVILY_SNIPPET_LENGTH:
                snippet = snippet[:TAVILY_SNIPPET_LENGTH].rsplit(" ", 1)[0] + "..."
            results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")
        result = "\n\n".join(results) if results else "No hotel results found"
        logger.info(f"Tavily tool: Found {len(results)} results")
        return result
    except Exception as e:
        logger.error(f"Tavily tool: Error - {str(e)}")
        return f"Error searching hotels: {str(e)}"


