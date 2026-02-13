from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An example agent that  will answer user query , If can not give answer clearly inform user',
    instruction = """
    You are a helpful assistant that provides information based on user queries.
    """,
    tools = [google_search]  # In-build tool


    # instruction='You are helpful assistant to answer user queries.'
    # instruction= 'Always ask user name before answering question',
    # instruction='Answer user questions to the best of your knowledge',
)
