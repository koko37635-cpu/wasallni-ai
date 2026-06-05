from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from typing import List, Tuple

class ForecastingService:
    """Service for demand forecasting and purchasing recommendations"""
    
    def __init__(self):
        self.daily_consumption = {}
        self.weekly_consumption = {}
        self.seasonal_factors = {}
    
    def calculate_daily_average(self, product_id: str, days: int = 30) -> float:
        """Calculate average daily consumption"""
        # TODO: Fetch from database and calculate
        return 8.0  # Example: 8 kg per day
    
    def calculate_weekly_average(self, product_id: str, weeks: int = 12) -> float:
        """Calculate average weekly consumption"""
        daily = self.calculate_daily_average(product_id)
        return daily * 7
    
    def calculate_seasonal_factor(self, product_id: str, month: int) -> float:
        """Calculate seasonal adjustment factor"""
        # TODO: Implement seasonal analysis
        return 1.0
    
    def forecast_demand(self, product_id: str, days_ahead: int = 7) -> List[dict]:
        """Forecast demand for next N days"""
        daily_avg = self.calculate_daily_average(product_id)
        seasonal = self.calculate_seasonal_factor(product_id, datetime.now().month)
        
        forecasts = []
        for i in range(days_ahead):
            date = datetime.now() + timedelta(days=i+1)
            predicted = daily_avg * seasonal + np.random.normal(0, daily_avg * 0.1)
            
            forecasts.append({
                'date': date.isoformat(),
                'predicted_demand': max(0, predicted),
                'confidence': 0.85,
                'recommendation': f'شراء {predicted:.1f} كجم'
            })
        
        return forecasts
    
    def recommend_purchase(self, product_id: str, current_stock: float) -> dict:
        """Recommend purchase order"""
        daily_avg = self.calculate_daily_average(product_id)
        days_remaining = current_stock / daily_avg if daily_avg > 0 else 0
        
        if days_remaining < 5:
            recommended_quantity = daily_avg * 7
            return {
                'current_stock': current_stock,
                'daily_consumption': daily_avg,
                'days_remaining': round(days_remaining, 1),
                'recommended_quantity': round(recommended_quantity, 1),
                'urgency': 'عالية' if days_remaining < 2 else 'متوسطة'
            }
        
        return None

forecasting_service = ForecastingService()
