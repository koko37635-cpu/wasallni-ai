from services.timeseries_forecast import ts_forecast
from services.advanced_anomaly import advanced_anomaly
from datetime import datetime, timedelta
from typing import List, Dict
import random

class AdvancedForecastingService:
    """خدمة التنبؤ المتقدمة"""
    
    def __init__(self):
        self.consumption_history = {}
        self.seasonal_factors = {}
    
    def generate_forecast_ensemble(self, product_id: str, days_ahead: int = 7, 
                                  consumption_history: List[float] = None) -> List[Dict]:
        """
        استخدام تجميع (Ensemble) من عدة نماذج
        """
        if consumption_history is None:
            consumption_history = [random.uniform(5, 15) for _ in range(30)]
        
        # استخدام عدة نماذج
        forecast1 = ts_forecast.double_exponential_smoothing(consumption_history, periods=days_ahead)
        forecast2 = ts_forecast.polynomial_regression_forecast(consumption_history, degree=2, periods=days_ahead)
        forecast3 = ts_forecast.arima_like_forecast(consumption_history, periods=days_ahead)
        
        # تجميع النتائج (متوسط موزون)
        ensemble_forecast = []
        for i in range(days_ahead):
            avg = (forecast1[i] * 0.4 + forecast2[i] * 0.35 + forecast3[i] * 0.25)
            ensemble_forecast.append(round(max(0, avg), 2))
        
        # حساب الثقة
        confidence = self._calculate_confidence(forecast1, forecast2, forecast3)
        
        # بناء النتائج
        forecasts = []
        for i, value in enumerate(ensemble_forecast):
            date = (datetime.now() + timedelta(days=i+1)).isoformat()
            forecasts.append({
                'date': date,
                'predicted_demand': value,
                'confidence': confidence[i],
                'recommendation': self._generate_recommendation(value)
            })
        
        return forecasts
    
    def _calculate_confidence(self, *forecasts) -> List[float]:
        """
        حساب درجة الثقة بناءً على توافق النماذج
        """
        confidence_scores = []
        for i in range(len(forecasts[0])):
            values = [f[i] for f in forecasts]
            avg = sum(values) / len(values)
            # حساب الانحراف المعياري النسبي
            variance = sum((v - avg) ** 2 for v in values) / len(values)
            std_dev = variance ** 0.5
            # كلما قل الاختلاف، زادت الثقة
            relative_std = std_dev / avg if avg > 0 else 0
            confidence = max(0.5, 1 - relative_std)
            confidence_scores.append(round(min(1, confidence), 2))
        
        return confidence_scores
    
    def _generate_recommendation(self, predicted_value: float) -> str:
        """
        إنشاء توصية على أساس التنبؤ
        """
        if predicted_value > 20:
            return "شراء كمية كبيرة - توقع طلب عالي"
        elif predicted_value > 12:
            return "شراء كمية متوسطة"
        elif predicted_value > 8:
            return "المخزون الحالي كافي"
        else:
            return "قد تكون هناك طلب منخفض"

advanced_forecasting = AdvancedForecastingService()
