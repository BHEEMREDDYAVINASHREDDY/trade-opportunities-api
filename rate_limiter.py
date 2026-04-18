import time
from fastapi import HTTPException

requests = {}

LIMIT = 5
WINDOW = 60

def check_limit(ip: str):
    now = time.time()
    
    if ip not in requests:
        requests[ip] = []
    
    requests[ip] = [t for t in requests[ip] if now - t < WINDOW]
    
    if len(requests[ip]) >= LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")
    
    requests[ip].append(now)