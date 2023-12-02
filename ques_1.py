from langchain import OpenAI, SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from env import OPENAI_API_KEY

dburi = "sqlite:///output.db"
db = SQLDatabase.from_uri(dburi)
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)


def driver1(industry_type):
    response = agent_executor.run(
        "What are the customers in"
        + industry_type
        + " industry that chose salesforce? Give the answer in form of bullet points ->"
    )
    return response
