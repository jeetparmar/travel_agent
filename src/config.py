import os
import logging
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from .constants import LLM_MODEL

logger = logging.getLogger(__name__)

load_dotenv()

llm = ChatGroq(model=LLM_MODEL)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

logger.info("Configuration loaded successfully")
logger.info(f"LLM model: {llm.model}")
