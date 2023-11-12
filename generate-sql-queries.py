import env
from langchain import OpenAI, SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType

dburi = "sqlite:///output.db"
db = SQLDatabase.from_uri(dburi)
llm = OpenAI(temperature=0,openai_api_key=env.OPENAI_API_KEY)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

response=agent_executor.run("""What are the customers in Retail industry that chose salesforce?
                 Give the answer in form of bullet points for easy grasp.""")
print(response)
