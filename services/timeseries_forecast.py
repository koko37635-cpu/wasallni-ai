import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from typing import List, Dict
from datetime import datetime, timedelta

class TimeSeriesForecast:
    """نماذج متقدمة للتنبؤ بسلاسل زمنية"""
    
    def __init__(self):
        self.models = {}
    
    def simple_exponential_smoothing(self, data: List[float], alpha: float = 0.3) -> List[float]:
        """
        التجانس الأسي البسيط
        """
        forecast = [data[0]]
        for i in range(1, len(data)):
            forecast.append(alpha * data[i-1] + (1 - alpha) * forecast[i-1])
        return forecast
    
    def double_exponential_smoothing(self, data: List[float], alpha: float = 0.3, beta: float = 0.1, periods: int = 7) -> List[float]:
        """
        التجانس الأسي المزدوج (Holt's Method)
        للتنبؤ مع الاتجاهات
        """
        # تهيئة
        level = data[0]
        trend = data[1] - data[0]
        
        history = [(level, trend)]
        
        # حساب السلسلة المتجانسة
        for i in range(1, len(data)):
            prev_level = level
            level = alpha * data[i] + (1 - alpha) * (level + trend)
            trend = beta * (level - prev_level) + (1 - beta) * trend
            history.append((level, trend))
        
        # التنبؤ
        last_level, last_trend = history[-1]
        forecast = [last_level + last_trend * (i + 1) for i in range(periods)]
        
        return forecast
    
    def polynomial_regression_forecast(self, data: List[float], degree: int = 2, periods: int = 7) -> List[float]:
        """
        استخدام الانحدار متعدد الحدود
        """
        X = np.arange(len(data)).reshape(-1, 1)
        y = np.array(data)
        
        # إنشاء النموذج
        poly = PolynomialFeatures(degree=degree)
        X_poly = poly.fit_transform(X)
        
        model = LinearRegression()
        model.fit(X_poly, y)
        
        # التنبؤ
        X_future = np.arange(len(data), len(data) + periods).reshape(-1, 1)
        X_future_poly = poly.transform(X_future)
        
        forecast = model.predict(X_future_poly).tolist()
        
        return [max(0, f) for f in forecast]  # تأكد من عدم وجود قيم سالبة
    
    def arima_like_forecast(self, data: List[float], p: int = 1, d: int = 1, periods: int = 7) -> List[float]:
        """
        نموذج ARIMA مبسط
        """
        # الفروق
        diff_data = np.diff(data, n=d).tolist()
        
        if len(diff_data) < p:
            return [data[-1]] * periods
        
        # استخدام AR بسيط
        forecast = []
        current_data = data[-p:].copy()
        
        for _ in range(periods):
            # حساب المتوسط المرجح
            next_val = sum(current_data) / len(current_data)
            forecast.append(max(0, next_val))
            current_data = current_data[1:] + [next_val]
        
        return forecast

ts_forecast = TimeSeriesForecast()
