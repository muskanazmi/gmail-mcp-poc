# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
# )

# import traceback
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from mcp_client import run_gmail_mcp

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ChatRequest(BaseModel):
#     message: str


    
# @app.post("/chat")
# async def chat(req: ChatRequest):
#     try:
#         reply = await run_gmail_mcp(req.message)
#         return {"reply": reply}
#     except Exception as e:
#         traceback.print_exc()
#         return {
#             "error": "Gmail MCP interaction failed",
#             "details": str(e)
#         }



import logging
import traceback
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mcp_client import run_gmail_mcp

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = FastAPI(title="Gmail MCP Chat API")

# CORS setup so frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"status": "Backend is running. Use /chat endpoint."}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        reply = await run_gmail_mcp(req.message)
        return {"reply": reply}
    except Exception as e:
        traceback.print_exc()
        return {
            "error": "Gmail MCP interaction failed",
            "details": str(e)
        }
