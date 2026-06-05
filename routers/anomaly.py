from fastapi import APIRouter
from models.schemas import AnomalyDetectionRequest
from services.anomaly_detection import anomaly_service

router = APIRouter(prefix="/api/anomaly", tags=["anomaly"])

@router.post("/detect")
async def detect_anomaly(request: AnomalyDetectionRequest):
    """
    كشف الحالات الشاذة (السرقة/الهدر)
    """
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
        return {'success': False, 'error': str(e)}

@router.get("/alerts/{product_id}")
async def get_alerts(product_id: str, days: int = 7):
    """
    احصل على التنبيهات للـ N يوم الأخير
    """
    try:
        # يمكن توسيع هذا لاحقاً
        return {
            'success': True,
            'data': [],
            'message': 'لا توجد تنبيهات حالياً'
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}
