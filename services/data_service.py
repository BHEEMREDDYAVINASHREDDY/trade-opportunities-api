import httpx

async def get_data(sector: str):
    url = "https://api.duckduckgo.com/"
    
    params = {
        "q": f"{sector} india market trends",
        "format": "json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()

    return data.get("AbstractText", "No data found")