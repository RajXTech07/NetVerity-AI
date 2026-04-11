from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.wifi import router as wifi_router
from app.routes.recommendation import router as rec_router

app = FastAPI(title="NetVerity.Ai")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(wifi_router)
app.include_router(rec_router)

@app.get("/")
def home():
    return {"message": "Welcome to NetVerity.AI"}