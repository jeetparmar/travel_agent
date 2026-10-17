import os
import logging
import requests
from dotenv import load_dotenv
from ..constants import (
    AVIATIONSTACK_API_URL,
    AVIATIONSTACK_LIMIT,
    AVIATIONSTACK_TIMEOUT,
)

logger = logging.getLogger(__name__)

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

if not API_KEY:
    raise ValueError("AVIATIONSTACK_API_KEY environment variable is not set")

def search_flights(query):
    logger.info(f"Flight tool: Searching for {query}")
    try:
        params = {"access_key": API_KEY, "limit": AVIATIONSTACK_LIMIT}
        response = requests.get(AVIATIONSTACK_API_URL, params=params, timeout=AVIATIONSTACK_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        flights = []
        if "data" in data:
            for flight in data["data"][:AVIATIONSTACK_LIMIT]:
                airline = flight.get("airline", {}).get("name", "unknown")
                departure = flight.get("departure", {}).get("airport", "unknown")
                arrival = flight.get("arrival", {}).get("airport", "unknown")
                status = flight.get("flight status", "unknown")
                flights.append(f"Airline: {airline}\nDeparture: {departure}\nArrival: {arrival}\nStatus: {status}")
        result = "\n".join(flights) if flights else "No flights found"
        logger.info(f"Flight tool: Found {len(flights)} flights")
        return result
    except requests.RequestException as e:
        logger.error(f"Flight tool: Error - {str(e)}")
        return f"Error searching flights: {str(e)}"

