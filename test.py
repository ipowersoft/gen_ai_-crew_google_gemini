import os
import serpapi

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SERPAPI_KEY")

client = serpapi.Client(api_key=api_key)
result = client.search(
    q="coffee",
    engine="google",
    location="Austin, Texas",
    hl="en",
    gl="us",
)

print(result)
