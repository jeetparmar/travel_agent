import logging
from langchain_core.messages import HumanMessage, SystemMessage
from ..config import llm
from ..state import TravelState
from ..constants import ITINERARY_SYSTEM_PROMPT

logger = logging.getLogger(__name__)


def itinerary_agent(state: TravelState):
    logger.info("Itinerary agent: Generating itinerary")
    prompt = f"""
    Create a travel itinerary.
    User Query:
    {state['user_query']}

    Flight Results:
    {state['flight_results']}

    Hotel Results:
    {state['hotel_results']}
    """

    response = llm.invoke(
        [
            SystemMessage(content=ITINERARY_SYSTEM_PROMPT),
            HumanMessage(content=prompt),
        ]
    )
    logger.info(f"Itinerary agent: Generated {len(response.content)} characters")
    return {
        "itinerary": response.content,
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }

