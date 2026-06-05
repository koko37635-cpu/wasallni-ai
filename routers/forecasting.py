from fastapi import APIRouter, HTTPException
from models.schemas import ForecastRequest, ForecastResponse
from services.forecasting import forecasting_service

router = APIRouter()

@router.post("/forecast")
async def forecast(request: ForecastRequest) -> dict:
    """Get demand forecast for a product"""
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
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/recommend/{product_id}")
async def recommend_purchase(product_id: str, current_stock: float):
    """Get purchase recommendation for a product"""
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
                'message': 'No purchase needed at this time'
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
