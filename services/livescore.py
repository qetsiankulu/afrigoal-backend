import os
import httpx
from dotenv import load_dotenv


"""
COMMAND LINE: 
source venv/bin/activate
uvicorn main:app --reload

"""

load_dotenv()

API_KEY = os.getenv("LIVESCORE_API_KEY")
API_SECRET = os.getenv("LIVESCORE_API_SECRET")

BASE_URL = "https://livescore-api.com/api-client"

async def fetch_teams():
    url = f"{BASE_URL}/competitions/participants.json"
    params = {
        "key": API_KEY,
        "secret": API_SECRET,
        "competition_id": 227,
        "season": 2025
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()
