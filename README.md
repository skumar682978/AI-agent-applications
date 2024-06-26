# AI-agent-applications

These three projects demonstrate the use of different assistant agents powered by the phi library and OpenAI's language models for specialized tasks:

## Data Analyst Agent:

- Purpose: Analyzes IMDb movie data.
- Components: Utilizes DuckDbAssistant and OpenAIChat.
- Setup: Loads environment variables for the OpenAI API key and defines a semantic model describing a "movies" table sourced from a CSV file.
- Functionality: Capable of responding to queries about the highest-rated movie in 2020 and different categories of movies, generating SQL code and presenting the responses in Markdown format.
  
## Financial Agent:

- Purpose: Provides financial data and analysis.
- Components: Uses the Assistant class with OpenAIChat and YFinanceTools.
- Setup: Loads the OpenAI API key and configures tools for fetching stock prices, analyst recommendations, company information, and news.
- Functionality: Can answer questions such as the current stock price of NVDA and perform comparative analysis between companies like NVDA and AMD, utilizing all available financial tools.
  
## RAG (Retrieval-Augmented Generation) Agent:

- Purpose: Retrieves information from a knowledge base of Thai recipes.
- Components: Incorporates the Assistant class, PDFUrlKnowledgeBase, and PgVector2.
- Setup: Loads the OpenAI API key and configures the knowledge base to read from a PDF URL, storing embeddings in a PostgreSQL database.
- Functionality: Capable of answering detailed questions about Thai recipes, such as the ingredients for Tom Kha Gai, by retrieving relevant information from the embedded knowledge base and enhancing responses with specific references from the PDF.
  
Each project showcases a different application of AI-assisted agents in data analysis, financial querying, and knowledge retrieval, leveraging OpenAI's advanced language models for diverse and specialized tasks.





