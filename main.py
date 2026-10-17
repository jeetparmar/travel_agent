import uuid
import logging
from langchain_core.messages import HumanMessage
from src.graph import compile_app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting Travel Agent")
    try:
        app = compile_app()
        config = {"configurable": {"thread_id": str(uuid.uuid4())}}

        user_input = input("Enter travel request: ").strip()
        if not user_input:
            print("Error: Travel request cannot be empty")
            return

        logger.info(f"Processing: {user_input}")
        result = app.invoke(
            {
                "messages": [HumanMessage(content=user_input)],
                "user_query": user_input,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0,
            },
            config=config,
        )

        logger.info(f"Completed. LLM calls: {result.get('llm_calls', 0)}")
        print("\nFINAL RESPONSE:\n")
        for msg in result["messages"]:
            print(msg.content)

    except KeyboardInterrupt:
        print("\nCancelled by user")
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

