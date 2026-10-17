# Travel Agent

A LangGraph-based travel planning agent that helps users plan trips by searching for flights, hotels, and generating comprehensive travel itineraries.

## Features

- **Flight Search**: Automatically searches for flights based on user queries
- **Hotel Recommendations**: Uses Tavily search to find the best hotels for the destination
- **Itinerary Generation**: Creates detailed travel itineraries using AI
- **Multi-Agent Workflow**: Orchestrates multiple specialized agents (flight, hotel, itinerary, final response)
- **State Persistence**: Uses PostgreSQL for persistent conversation state
- **Conversation Memory**: Maintains conversation history across sessions

## Architecture

The application uses LangGraph to coordinate multiple agents in a sequential workflow:

1. **Flight Agent**: Searches for flights based on the user's travel request
2. **Hotel Agent**: Finds hotel recommendations using Tavily search
3. **Itinerary Agent**: Generates a detailed travel itinerary using LLM
4. **Final Agent**: Synthesizes all information into a comprehensive travel response

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Groq API key
- Tavily API key
- AviationStack API key

## Installation

1. Clone the repository and navigate to the project directory:

```bash
cd travel_agent
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
# OR
pip install -e .
```

4. Set up a PostgreSQL database:

```bash
# Create a database
createdb langgraph_memory
# The checkpointer will automatically set up necessary tables on first run
```

## Configuration

Create a `.env` file in the project root with the following environment variables:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
```

## Project Structure

```
travel_agent/
├── main.py              # CLI entry point
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project configuration
├── .gitignore          # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── config.py        # Configuration (LLM, database URL)
│   ├── state.py         # TravelState definition
│   ├── constants.py     # Application constants (new)
│   ├── graph.py         # LangGraph workflow definition and compilation
│   ├── agents/
│   │   ├── __init__.py  # Agent exports
│   │   ├── flight_agent.py  # Flight search agent
│   │   ├── hotel_agent.py   # Hotel search agent
│   │   ├── itinerary_agent.py  # Itinerary generation agent
│   │   └── final_agent.py   # Final response agent
│   └── tools/
│       ├── __init__.py
│       ├── flight_tool.py   # Flight search functionality
│       └── tavily_tool.py   # Tavily search integration for hotels
├── .env                 # Environment variables (not committed)
└── README.md            # This file
```

## How to Run

### Step-by-Step Instructions

1. **Set up PostgreSQL database**:

   ```bash
   # Install PostgreSQL if not already installed
   # Create a database for the travel agent
   createdb langgraph_memory
   ```

2. **Configure environment variables**:

   ```bash
   # Create .env file in the project root
   cat > .env << EOF
   DATABASE_URL=postgresql://$(whoami)@localhost:5432/langgraph_memory
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   AVIATIONSTACK_API_KEY=your_aviationstack_api_key_here
   EOF
   ```

3. **Install dependencies**:

   ```bash
   # Activate virtual environment (if created)
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python main.py
   ```

5. **Enter your travel request**:

   ```
   Enter travel request: I want to travel from New York to Paris next week
   ```

6. **View the results**:
   The agent will process your request through the workflow and display:
   - Flight search results
   - Hotel recommendations
   - Generated itinerary
   - Final comprehensive travel response

### Example Output

```
2024-10-17 10:30:00 - __main__ - INFO - Starting Travel Agent
2024-10-17 10:30:01 - src.config - INFO - Configuration loaded successfully
2024-10-17 10:30:01 - src.config - INFO - LLM model: openai/gpt-oss-120b
2024-10-17 10:30:02 - src.graph - INFO - Creating LangGraph workflow
2024-10-17 10:30:02 - src.graph - INFO - Graph structure: START -> flight -> hotel -> itinerary -> final -> END
2024-10-17 10:30:02 - src.graph - INFO - Compiling LangGraph application
2024-10-17 10:30:03 - src.graph - INFO - Connecting to PostgreSQL database
2024-10-17 10:30:03 - src.graph - INFO - Application compiled successfully
Enter travel request: I want to travel from New York to Paris next week
2024-10-17 10:30:10 - __main__ - INFO - Processing: I want to travel from New York to Paris next week
...

FINAL RESPONSE:

[Your comprehensive travel plan here]
```

## Usage

### Integration with Streamlit

The application supports integration with Streamlit for a web interface. The compiled app with PostgreSQL checkpointer can be imported and used in a Streamlit application:

```python
from src.graph import compile_app

app = compile_app()
# Use app in your Streamlit interface
```

## API Keys

- **Groq API**: Get your API key from [Groq Console](https://console.groq.com/)
- **Tavily API**: Get your API key from [Tavily](https://tavily.com/)
- **AviationStack API**: Get your API key from [AviationStack](https://aviationstack.com/)

## How It Works

1. The user provides a travel query
2. The flight agent searches for relevant flights
3. The hotel agent uses Tavily to find hotel options
4. The itinerary agent uses the LLM to create a detailed travel plan
5. The final agent synthesizes all information into a cohesive response
6. All state is persisted in PostgreSQL for conversation continuity

## License

MIT
