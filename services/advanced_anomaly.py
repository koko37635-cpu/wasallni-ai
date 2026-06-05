import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from typing import Dict, List
from datetime import datetime, timedelta

class AdvancedAnomalyDetection:
    """خوارزميات متقدمة لكشف الحالات الشاذة"""
    
    def __init__(self, contamination: float = 0.1):
        self.contamination = contamination
        self.scaler = StandardScaler()
        self.iso_forest = IsolationForest(contamination=contamination, random_state=42)
    
    def detect_with_ml(self, consumption_history: List[float]) -> Dict:
        """
        استخدام Isolation Forest لكشف الحالات الشاذة
        """
        if len(consumption_history) < 10:
            return {
                'is_anomaly': False,
                'message': 'بيانات غير كافية للتحليل'
            }
        
        # تحويل البيانات
        X = np.array(consumption_history).reshape(-1, 1)
        X_scaled = self.scaler.fit_transform(X)
        
        # التنبؤ
        predictions = self.iso_forest.fit_predict(X_scaled)
        
        # حساب نسبة الحالات الشاذة
        anomalies = np.where(predictions == -1)[0]
        anomaly_percentage = len(anomalies) / len(consumption_history) * 100
        
        return {
            'is_anomaly': len(anomalies) > 0,
            'anomaly_count': len(anomalies),
            'anomaly_percentage': round(anomaly_percentage, 2),
            'anomaly_indices': anomalies.tolist(),
            'severity': 'high' if anomaly_percentage > 20 else 'medium' if anomaly_percentage > 10 else 'low'
        }
    
    def detect_seasonal_anomaly(self, consumption_history: List[float], season_days: int = 7) -> Dict:
        """
        كشف الحالات الشاذة الموسمية
        """
        if len(consumption_history) < season_days * 2:
            return {'is_anomaly': False, 'message': 'بيانات غير كافية'}
        
        # حساب المتوسط الموسمي
        seasonal_avg = np.mean(consumption_history[-season_days:])
        seasonal_std = np.std(consumption_history[-season_days:])
        
        # فحص آخر قيمة
        last_value = consumption_history[-1]
        z_score = (last_value - seasonal_avg) / seasonal_std if seasonal_std > 0 else 0
        
        return {
            'is_anomaly': abs(z_score) > 2,  # 2 sigma
            'z_score': round(z_score, 2),
            'seasonal_avg': round(seasonal_avg, 2),
            'last_value': round(last_value, 2),
            'deviation_percentage': round(((last_value - seasonal_avg) / seasonal_avg * 100) if seasonal_avg > 0 else 0, 2)
        }

advanced_anomaly = AdvancedAnomalyDetection()
