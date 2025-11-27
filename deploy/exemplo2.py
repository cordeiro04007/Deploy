from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.vectordb.chroma import ChromaDb
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.os import AgentOS
import asyncio
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# RAG ==================================================
# Initialize ChromaDB
vector_db = ChromaDb(
    collection="pdf_agent",
    path="tmp/chromadb",
    persistent_client=True
)

knowledge = Knowledge(vector_db=vector_db)
# STORAGE ===============================================
# Setup the SQLite database
db = SqliteDb(session_table="agent_session", db_file = 'tmp/agent.db')

# AGENT ================================================
agent = Agent(
    id = 'Agente_PDF',
    name="Agente de PDF",
    model=OpenAIChat(id="gpt-5-nano", api_key=os.getenv("OPENAI_API_KEY")),
    db = db,
    knowledge= knowledge,
    instructions="Você deve chamar o usuário de senhor",
    description='',
    search_knowledge=True,
    num_history_runs=3,
    debug_mode=True,
    enable_user_memories=True,
)
#AGENTOS
agent_os = AgentOS(
    name = 'Agente de PDF',
    agents=[agent],
)

app = agent_os.get_app()
#RUN
if __name__=='__main__':
    knowledge.add_content(
        url = 'https://s3.sa-east-1.amazonaws.com/static.grendene.aatb.com.br/releases/2446_PR_3T25.pdf',
        metadata = {'source': 'Grande', 'type': 'pdf', 'descriptiion': 'Relatório Trimestral 3T25'},
        skip_if_exists = True,
        reader= PDFReader(),
    )
    agent_os.serve(app='exemplo2:app', reload=True)











