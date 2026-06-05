from fastapi import APIRouter
from models.schemas import ForecastRequest, ForecastResponse
from services.forecasting import forecasting_service

router = APIRouter(prefix="/api/forecasting", tags=["forecasting"])

@router.post("/forecast")
async def forecast(request: ForecastRequest):
    """
    التنبؤ بالاستهلاك للـ N يوم القادمة
    """
    try:
        forecast_data = forecasting_service.forecast_demand(
            request.product_id,
            request.days_ahead
        )
        return {
            'success': True,
            'data': forecast_data
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

@router.get("/recommend/{product_id}")
async def recommend_purchase(product_id: str, current_stock: float):
    """
    احصل على توصيات الشراء
    """
    try:
        recommendation = forecasting_service.recommend_purchase(
            product_id,
            current_stock
        )
        if recommendation:
            return {
                'success': True,
                'data': recommendation
            }
        else:
            return {
                'success': True,
                'data': None,
                'message': 'لا توجد حاجة لشراء في الوقت الحالي'
            }
    except Exception as e:
        return {'success': False, 'error': str(e)}
