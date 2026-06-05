import numpy as np
from typing import Tuple

class AnomalyDetectionService:
    """Service for detecting theft and waste in inventory"""
    
    def __init__(self, threshold: float = 0.95):
        self.threshold = threshold
    
    def detect_anomaly(self, actual_consumption: float, expected_consumption: float) -> dict:
        """Detect anomalies in consumption patterns"""
        if expected_consumption == 0:
            return {
                'is_anomaly': False,
                'difference_percentage': 0,
                'severity': 'none',
                'alert_message': 'No expected consumption data'
            }
        
        difference = actual_consumption - expected_consumption
        difference_percentage = (difference / expected_consumption) * 100
        
        is_anomaly = abs(difference_percentage) > (1 - self.threshold) * 100
        severity = self._calculate_severity(difference_percentage)
        
        alert_message = self._generate_alert_message(
            actual_consumption,
            expected_consumption,
            difference_percentage,
            severity
        )
        
        return {
            'is_anomaly': is_anomaly,
            'difference_percentage': round(difference_percentage, 2),
            'actual': actual_consumption,
            'expected': expected_consumption,
            'severity': severity,
            'alert_message': alert_message
        }
    
    def _calculate_severity(self, percentage: float) -> str:
        """Calculate severity level"""
        abs_percent = abs(percentage)
        if abs_percent > 20:
            return 'high'
        elif abs_percent > 10:
            return 'medium'
        else:
            return 'low'
    
    def _generate_alert_message(self, actual: float, expected: float, 
                               percentage: float, severity: str) -> str:
        """Generate alert message"""
        if actual > expected:
            return f"تحذير: الاستهلاك الفعلي ({actual:.1f}) أعلى من المتوقع ({expected:.1f}) بنسبة {percentage:.1f}%. احتمال هدر أو فقد بالمخزون."
        else:
            return f"ملاحظة: الاستهلاك الفعلي ({actual:.1f}) أقل من المتوقع ({expected:.1f}) بنسبة {abs(percentage):.1f}%."

anomaly_service = AnomalyDetectionService()
