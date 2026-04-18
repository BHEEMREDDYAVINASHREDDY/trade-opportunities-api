import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

async def analyze(sector: str, data: str):
    
    if not API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API key missing")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    prompt = f"""
You are a professional market analyst.

Analyze the {sector} sector in India based on this data:

{data}

IMPORTANT:
- Use only factual insights
- If data is limited, say "Limited data available"

Generate a structured MARKDOWN report with:

# {sector.title()} Sector Analysis (India)

## Overview
## Current Trends
## Opportunities
## Risks
## Conclusion
"""

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, json=body)

        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Gemini API error")

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))