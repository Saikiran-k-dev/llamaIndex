import os
from dotenv import load_dotenv
import openai
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from llama_index import KeywordTableIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import OpenAI

llm = OpenAI(temperature=0, model="text-davinci-002")
service_context = ServiceContext.from_defaults(llm=llm)

documents = SimpleDirectoryReader("paul_graham_essay/data").load_data()
index = KeywordTableIndex.from_documents(
    documents=documents, service_context=service_context
)
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do after his time at Y Combinator?")
