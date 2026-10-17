import logging
from langchain_core.messages import AIMessage
from ..tools.tavily_tool import tavily_search
from ..state import TravelState
from ..constants import HOTEL_AGENT_MESSAGE

logger = logging.getLogger(__name__)


def hotel_agent(state: TravelState):
    query = f"Best hotels for {state['user_query']}"
    logger.info(f"Hotel agent: Searching for {query}")
    hotel_results = tavily_search(query)
    logger.info(f"Hotel agent: Found {len(hotel_results)} characters of results")
    return {
        "hotel_results": hotel_results,
        "messages": [AIMessage(content=HOTEL_AGENT_MESSAGE)],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }

