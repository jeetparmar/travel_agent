import logging
from langchain_core.messages import AIMessage
from ..tools.flight_tool import search_flights
from ..state import TravelState
from ..constants import FLIGHT_AGENT_MESSAGE

logger = logging.getLogger(__name__)


def flight_agent(state: TravelState):
    logger.info(f"Flight agent: Searching for {state['user_query']}")
    flight_data = search_flights(state["user_query"])
    logger.info(f"Flight agent: Found {len(flight_data)} characters of results")
    return {
        "flight_results": flight_data,
        "messages": [AIMessage(content=FLIGHT_AGENT_MESSAGE)],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }

