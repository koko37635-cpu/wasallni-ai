from fastapi import APIRouter
from services.analytics import analytics_service

router = APIRouter(prefix="/api/analytics", tags=["analytics"])

@router.get("/daily-report")
async def get_daily_report(branch_id: str = None):
    """
    احصل على التقرير اليومي
    """
    try:
        report = analytics_service.generate_daily_report(branch_id)
        return {
            'success': True,
            'data': report
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

@router.get("/branches-performance")
async def get_branches_performance():
    """
    احصل على أداء جميع الفروع
    """
    try:
        performance = analytics_service.get_branch_performance()
        return {
            'success': True,
            'data': performance
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

@router.get("/sales-trends")
async def get_sales_trends(days: int = 30, branch_id: str = None):
    """
    احصل على اتجاهات المبيعات
    """
    try:
        trends = analytics_service.get_sales_trends(days, branch_id)
        return {
            'success': True,
            'data': trends
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}
