from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

load_dotenv()

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o",api_key=os.getenv("OpenAI_key")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("What is the stock price of NVDA")
assistant.print_response("Write a comparison between NVDA and AMD, use all tools available.")