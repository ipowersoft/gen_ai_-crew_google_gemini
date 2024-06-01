## https://serper.dev/

from dotenv import load_dotenv

load_dotenv()
import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
api_key = os.environ["SERPER_API_KEY"]

print(api_key)

from crewai_tools import SerperDevTool

# client = serpapi.Client(api_key=api_key)

# Initialize the tool for internet searching capabilities
tool = SerperDevTool(api_key=api_key)
