from fastapi import APIRouter, HTTPException
from models.schemas import DailyReportRequest
from services.analytics import analytics_service

router = APIRouter()

@router.get("/daily-report")
async def get_daily_report(branch_id: str = None):
    """Get daily analytics report"""
    try:
        report = analytics_service.generate_daily_report(branch_id)
        return {
            'success': True,
            'data': report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/branches-performance")
async def get_branches_performance():
    """Get performance metrics for all branches"""
    try:
        performance = analytics_service.get_branch_performance()
        return {
            'success': True,
            'data': performance
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sales-trends")
async def get_sales_trends(days: int = 30):
    """Get sales trends"""
    try:
        trends = analytics_service.get_sales_trends(days)
        return {
            'success': True,
            'data': trends
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
