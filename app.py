from starlette.routing import Mount, Router 
import uvicorn
from config import settings 
from database.database import *
from fastapi import FastAPI, Depends, Request, Form, HTTPException
from starlette.responses import Response
import json
import sys
from routes.Employee import router as StudentRouter
from starlette.applications import Starlette

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

app.include_router(StudentRouter, tags=["idp"], prefix="/idp")


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
