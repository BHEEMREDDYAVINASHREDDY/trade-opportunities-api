from fastapi import FastAPI, Request, Depends
from auth import verify_token, create_token
from rate_limiter import check_limit
from services.data_service import get_data
from services.ai_service import analyze
from utils.validator import validate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/auth")
def get_token():
    return {"token": create_token()}

@app.get("/analyze/{sector}")
async def analyze_sector(
    sector: str,
    request: Request,
    auth=Depends(verify_token)
):
    ip = request.client.host
    check_limit(ip)

    sector = validate(sector)

    data = await get_data(sector)
    report = await analyze(sector, data)

    return {
        "sector": sector,
        "report": report
    }