from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ForecastRequest(BaseModel):
    product_id: str
    days_ahead: int = 7
    
class ForecastResponse(BaseModel):
    product_id: str
    date: str
    predicted_demand: float
    confidence: float
    recommendation: str

class AnomalyDetectionRequest(BaseModel):
    actual_consumption: float
    expected_consumption: float
    product_id: str

class AnomalyResponse(BaseModel):
    is_anomaly: bool
    difference_percentage: float
    severity: str  # 'low', 'medium', 'high'
    alert_message: str

class DailyReportRequest(BaseModel):
    branch_id: Optional[str] = None
    date: str

class DailyReportResponse(BaseModel):
    date: str
    total_sales: float
    orders_count: int
    avg_order_value: float
    insights: List[str]
