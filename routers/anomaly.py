from fastapi import APIRouter, HTTPException
from models.schemas import AnomalyDetectionRequest, AnomalyResponse
from services.anomaly_detection import anomaly_service

router = APIRouter()

@router.post("/detect")
async def detect_anomaly(request: AnomalyDetectionRequest):
    """Detect anomalies in consumption"""
    try:
        result = anomaly_service.detect_anomaly(
            request.actual_consumption,
            request.expected_consumption
        )
        return {
            'success': True,
            'data': result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/alerts/{product_id}")
async def get_alerts(product_id: str):
    """Get anomaly alerts for a product"""
    # TODO: Fetch alerts from database
    return {
        'success': True,
        'data': []
    }
