import psycopg
import logging
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver

from .state import TravelState
from .agents import flight_agent, hotel_agent, itinerary_agent, final_agent
from .config import DATABASE_URL
from .constants import (
    FLIGHT_AGENT_NAME,
    HOTEL_AGENT_NAME,
    ITINERARY_AGENT_NAME,
    FINAL_AGENT_NAME,
)

logger = logging.getLogger(__name__)


def create_graph():
    logger.info("Creating LangGraph workflow")
    graph = StateGraph(TravelState)

    graph.add_node(FLIGHT_AGENT_NAME, flight_agent)
    graph.add_node(HOTEL_AGENT_NAME, hotel_agent)
    graph.add_node(ITINERARY_AGENT_NAME, itinerary_agent)
    graph.add_node(FINAL_AGENT_NAME, final_agent)

    graph.add_edge(START, FLIGHT_AGENT_NAME)
    graph.add_edge(FLIGHT_AGENT_NAME, HOTEL_AGENT_NAME)
    graph.add_edge(HOTEL_AGENT_NAME, ITINERARY_AGENT_NAME)
    graph.add_edge(ITINERARY_AGENT_NAME, FINAL_AGENT_NAME)
    graph.add_edge(FINAL_AGENT_NAME, END)

    logger.info("Graph structure: START -> flight -> hotel -> itinerary -> final -> END")
    return graph


def compile_app():
    logger.info("Compiling LangGraph application")
    graph = create_graph()

    try:
        logger.info("Connecting to PostgreSQL database")
        _conn = psycopg.connect(DATABASE_URL, autocommit=True)
        checkpointer = PostgresSaver(_conn)
        checkpointer.setup()

        app = graph.compile(checkpointer=checkpointer)
        logger.info("Application compiled successfully")
        return app
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise RuntimeError(f"Failed to compile app: {str(e)}")


