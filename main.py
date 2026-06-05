from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Wasallni AI",
    description="AI Analytics & Forecasting API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Wasallni AI Service Running"}

@app.get("/health")
async def health():
    return {"status": "OK"}

# Routes will be imported here
# from routers import forecasting, analytics, detection
# app.include_router(forecasting.router, prefix="/api/forecasting", tags=["forecasting"])
# app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
# app.include_router(detection.router, prefix="/api/detection", tags=["detection"])

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
