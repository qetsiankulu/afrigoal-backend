from fastapi import FastAPI, HTTPException
from services.livescore import fetch_teams

app = FastAPI()

@app.get("/afcon/teams")
async def get_teams():
    try:
        data = await fetch_teams()
        return {"teams": data["data"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
