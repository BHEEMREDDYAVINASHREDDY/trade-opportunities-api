from fastapi import Header, HTTPException
import jwt
from datetime import datetime, timedelta

SECRET = "secret123"

def create_token():
    payload = {
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")