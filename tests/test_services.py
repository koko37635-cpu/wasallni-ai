# Test file for AI services

import sys
sys.path.append('.')

from services.advanced_forecasting import advanced_forecasting
from services.advanced_anomaly import advanced_anomaly
from services.timeseries_forecast import ts_forecast

def test_forecasting():
    print("\n=== اختبار التنبؤ ===")
    
    # بيانات تاريخية وهمية
    consumption_data = [10, 12, 11, 13, 14, 12, 11, 13, 15, 14, 12, 11, 13, 12, 14, 15, 13, 12, 14, 13, 12, 11, 10, 12, 13, 14, 15, 12, 11, 13]
    
    forecasts = advanced_forecasting.generate_forecast_ensemble(
        product_id='test-product',
        days_ahead=7,
        consumption_history=consumption_data
    )
    
    print("\nالتنبؤات للـ 7 أيام القادمة:")
    for forecast in forecasts:
        print(f"التاريخ: {forecast['date'][:10]}")
        print(f"الطلب المتوقع: {forecast['predicted_demand']} كجم")
        print(f"درجة الثقة: {forecast['confidence']*100:.1f}%")
        print(f"التوصية: {forecast['recommendation']}")
        print("-" * 50)

def test_anomaly_detection():
    print("\n=== اختبار كشف الحالات الشاذة ===")
    
    # بيانات استهلاك
    consumption_history = [10, 11, 12, 10, 11, 12, 11, 50, 12, 11, 10, 12, 11]  # قيمة شاذة في المنتصف
    
    result = advanced_anomaly.detect_with_ml(consumption_history)
    print(f"\nنتيجة كشف الحالات الشاذة:")
    print(f"وجود حالات شاذة: {'نعم' if result['is_anomaly'] else 'لا'}")
    print(f"عدد الحالات الشاذة: {result.get('anomaly_count', 0)}")
    print(f"نسبة الشذوذ: {result.get('anomaly_percentage', 0)}%")
    print(f"مستوى الخطورة: {result.get('severity', 'unknown')}")

def test_seasonal_anomaly():
    print("\n=== اختبار الحالات الشاذة الموسمية ===")
    
    consumption_history = [10, 11, 12, 10, 11, 12, 11, 12, 10, 11, 12, 10, 11, 100]  # قيمة شاذة جداً
    
    result = advanced_anomaly.detect_seasonal_anomaly(consumption_history, season_days=7)
    print(f"\nالنتيجة:")
    print(f"حالة شاذة: {'نعم' if result['is_anomaly'] else 'لا'}")
    print(f"Z-Score: {result.get('z_score', 0)}")
    print(f"المتوسط الموسمي: {result.get('seasonal_avg', 0)}")
    print(f"نسبة الانحراف: {result.get('deviation_percentage', 0)}%")

if __name__ == "__main__":
    print("🚀 بدء الاختبارات...")
    test_forecasting()
    test_anomaly_detection()
    test_seasonal_anomaly()
    print("\n✅ انتهت جميع الاختبارات!")
