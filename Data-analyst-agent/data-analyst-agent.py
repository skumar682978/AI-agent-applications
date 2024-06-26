import json

from phi.llm.openai import OpenAIChat
from phi.assistant.duckdb import DuckDbAssistant
import os
from dotenv import load_dotenv

load_dotenv()

data_analyst = DuckDbAssistant(
    llm=OpenAIChat(model="gpt-4o",api_key=os.getenv("OpenAI_key")),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "movies",
                    "description": "Contains information about movies from IMDB.",
                    "path": "imdb-top-1000.csv",
                }
            ]
        }
    ),
)

data_analyst.print_response("Highest rated movie in 2020? Show me the SQL.", markdown=True)
data_analyst.print_response("Different categories of movies", markdown=True)