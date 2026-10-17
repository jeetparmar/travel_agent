import logging
from langchain_core.messages import HumanMessage
from ..config import llm
from ..state import TravelState

logger = logging.getLogger(__name__)


def final_agent(state: TravelState):
    logger.info("Final agent: Generating final response")
    final_prompt = f"""
    Generate final travel response.

    Flights:
    {state['flight_results']}

    Hotels:
    {state['hotel_results']}

    Itinerary:
    {state['itinerary']}
    """

    response = llm.invoke([HumanMessage(content=final_prompt)])
    logger.info(f"Final agent: Generated {len(response.content)} characters")
    return {"messages": [response], "llm_calls": state.get("llm_calls", 0) + 1}

