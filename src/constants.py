# LLM Configuration
LLM_MODEL = "openai/gpt-oss-120b"

# Agent System Prompts
ITINERARY_SYSTEM_PROMPT = "You are an expert travel planner"

# API Configuration
AVIATIONSTACK_API_URL = "http://api.aviationstack.com/v1/flights"
AVIATIONSTACK_LIMIT = 5
AVIATIONSTACK_TIMEOUT = 10

TAVILY_MAX_RESULTS = 5
TAVILY_SNIPPET_LENGTH = 300

# Agent Names
FLIGHT_AGENT_NAME = "flight_agent"
HOTEL_AGENT_NAME = "hotel_agent"
ITINERARY_AGENT_NAME = "itinerary_agent"
FINAL_AGENT_NAME = "final_agent"

# Agent Messages
FLIGHT_AGENT_MESSAGE = "Flight search completed"
HOTEL_AGENT_MESSAGE = "Hotel search completed"


