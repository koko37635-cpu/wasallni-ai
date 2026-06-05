from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from routers import forecasting, anomaly, analytics

load_dotenv()

app = FastAPI(
    title="Wasallni AI",
    description="AI Analytics & Forecasting API for Restaurant Management",
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
    return {
        "message": "Wasallni AI Service Running",
        "version": "1.0.0",
        "endpoints": {
            "forecasting": "/docs#/forecasting",
            "anomaly": "/docs#/anomaly",
            "analytics": "/docs#/analytics"
        }
    }

@app.get("/health")
async def health():
    return {"status": "OK", "service": "AI"}

# Include routers
app.include_router(forecasting.router)
app.include_router(anomaly.router)
app.include_router(analytics.router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
