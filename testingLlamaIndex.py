import os
from dotenv import load_dotenv
import openai
load_dotenv()
from llama_index.agent import OpenAIAgent

openai.api_key = os.getenv("OPENAI_API_KEY")

from llama_hub.tools.google_calendar.base import GoogleCalendarToolSpec
tool_spec = GoogleCalendarToolSpec()
agent = OpenAIAgent.from_tools(tool_spec.to_tool_list(), verbose=True)
agent.chat('what is the first thing on my calendar today')
