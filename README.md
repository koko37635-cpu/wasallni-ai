# 🍕 وصللي - Wasallni

**منصة ذكية لإدارة مطاعم البيتزا**

> نظام متكامل يجمع بين الذكاء الاصطناعي وإدارة الأعمال لتحسين عمليات المطاعم وزيادة الأرباح

---

## 🎯 الميزات الرئيسية

### 🤖 الذكاء الاصطناعي
- **التنبؤ بالطلب**: توقع الاستهلاك بدقة عالية للمواد الخام
- **كشف الشذوذ**: اكتشاف السرقة والهدر تلقائياً
- **تحليل المبيعات**: رؤى آنية عن أداء الفروع
- **توصيات الشراء**: اقتراحات ذكية لطلبات المواد

### 📊 لوحة المراقبة
- عرض المبيعات اليومية والشهرية
- مقارنة أداء الفروع
- تنبيهات فورية للمشاكل
- رسوم بيانية تفاعلية

### 📦 إدارة المخزون
- تتبع المواد الخام تلقائياً
- إنذارات عند انخفاض المخزون
- إدارة العلاقة مع الموردين
- تقارير الاستهلاك

### 💰 تحليل الأرباح
- حساب صافي الربح الفعلي
- تتبع التكاليف والمصروفات
- تحليل الهوامش الربحية
- تقارير مالية شاملة

### 📍 إدارة الفروع
- مراقبة أداء كل فرع
- تقييمات العملاء
- إحصائيات الموظفين
- خريطة تفاعلية للفروع

---

## 🏗️ البنية المعمارية

```
wasallni/
├── wasallni-backend/       # Node.js + Express + PostgreSQL
│   ├── src/
│   │   ├── controllers/    # معالجات الطلبات
│   │   ├── services/       # خدمات الأعمال
│   │   ├── middleware/     # وسيط (Auth, ErrorHandling)
│   │   ├── routes/         # مسارات API
│   │   └── database/       # اتصال قاعدة البيانات
│   ├── database/
│   │   ├── schema.sql      # هيكل قاعدة البيانات
│   │   └── seed.sql        # البيانات الأولية
│   └── package.json
│
├── wasallni-frontend/      # React + TypeScript + Tailwind
│   ├── src/
│   │   ├── components/     # مكونات React
│   │   ├── pages/          # الصفحات
│   │   ├── stores/         # Zustand State Management
│   │   ├── styles/         # Tailwind CSS
│   │   └── utils/          # دوال مساعدة
│   └── package.json
│
└── wasallni-ai/            # Python + FastAPI + ML
    ├── services/
    │   ├── forecasting.py              # التنبؤ الأساسي
    │   ├── advanced_forecasting.py     # تجميع النماذج
    │   ├── anomaly_detection.py        # كشف الشذوذ البسيط
    │   ├── advanced_anomaly.py         # ML-based كشف
    │   ├── timeseries_forecast.py      # نماذج السلاسل الزمنية
    │   └── analytics.py                # التحليلات
    ├── routers/
    │   ├── forecasting.py
    │   ├── anomaly.py
    │   └── analytics.py
    ├── models/
    │   └── schemas.py                  # Pydantic Schemas
    ├── tests/
    │   └── test_services.py
    ├── requirements.txt
    └── main.py
```

---

## 🚀 البدء السريع

### المتطلبات
- Node.js 16+
- Python 3.9+
- PostgreSQL 12+
- Docker (اختياري)

### التثبيت

#### 1. Backend Setup
```bash
cd wasallni-backend
npm install
cp .env.example .env
# عدّل .env بالقيم الصحيحة
npm run dev
```

#### 2. Frontend Setup
```bash
cd wasallni-frontend
npm install
npm start
```

#### 3. AI Service Setup
```bash
cd wasallni-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 4. قاعدة البيانات
```bash
psql -U postgres -d wasallni -f database/schema.sql
psql -U postgres -d wasallni -f database/seed.sql
```

---

## 📚 التوثيق

### API Documentation
- **Backend API**: http://localhost:3000/api/docs
- **AI Service**: http://localhost:8000/docs

### قواعد البيانات
راجع `database/schema.sql` لفهم بنية الجداول

### نماذج الـ AI
انظر `wasallni-ai/tests/test_services.py` للأمثلة

---

## 🔌 API Endpoints

### Authentication
```
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/logout
```

### Orders
```
GET    /api/orders
POST   /api/orders
GET    /api/orders/:id
PUT    /api/orders/:id
```

### Inventory
```
GET    /api/inventory
POST   /api/inventory
PUT    /api/inventory/:id
GET    /api/inventory/low-stock
```

### Analytics
```
GET    /api/analytics/daily-report
GET    /api/analytics/branch-performance
GET    /api/analytics/sales-trends
```

### AI Services
```
POST   /api/forecasting/forecast
GET    /api/forecasting/recommend/:product_id
POST   /api/anomaly/detect
GET    /api/anomaly/alerts/:product_id
```

---

## 🧠 نماذج الذكاء الاصطناعي

### التنبؤ (Forecasting)
- **Double Exponential Smoothing**: للاتجاهات
- **Polynomial Regression**: للأنماط المعقدة
- **ARIMA**: للسلاسل الزمنية
- **Ensemble**: دمج النماذج الثلاثة

### كشف الشذوذ (Anomaly Detection)
- **Statistical Methods**: Z-Score
- **Isolation Forest**: ML-based
- **Seasonal Analysis**: الأنماط الموسمية

---

## 📊 أمثلة الاستخدام

### التنبؤ بالطلب
```bash
curl -X POST http://localhost:8000/api/forecasting/forecast \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1", "days_ahead": 7}'
```

### كشف الشذوذ
```bash
curl -X POST http://localhost:8000/api/anomaly/detect \
  -H "Content-Type: application/json" \
  -d '{
    "actual_consumption": 50,
    "expected_consumption": 10,
    "product_id": "1"
  }'
```

### جلب التقرير اليومي
```bash
curl http://localhost:3000/api/analytics/daily-report
```

---

## 🔒 الأمان

- **JWT Authentication**: لجميع الطلبات
- **Role-Based Access**: (Admin, Manager, Staff, Delivery)
- **Rate Limiting**: حماية من الإساءة
- **HTTPS**: في الإنتاج
- **Input Validation**: Pydantic & JOI

---

## 📈 الأداء

- **Response Time**: < 200ms
- **Database Queries**: مفهرسة محسّنة
- **Caching**: Redis (اختياري)
- **Load Balancing**: Nginx

---

## 🧪 الاختبار

### اختبارات الـ AI
```bash
cd wasallni-ai
python -m pytest tests/
# أو
python tests/test_services.py
```

---

## 🤝 المساهمة

1. Fork المشروع
2. انشئ فرع (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add AmazingFeature'`)
4. Push للفرع (`git push origin feature/AmazingFeature`)
5. افتح Pull Request

---

## 📝 الترخيص

هذا المشروع مرخص تحت MIT License

---

## 📞 التواصل

- **Email**: support@wasallni.com
- **GitHub Issues**: للمشاكل والاقتراحات
- **Telegram**: @wasallni_team

---

## 🎉 شكراً!

شكراً لاستخدام وصللي! نتطلع لتحسين عملك. 🚀

---

**آخر تحديث**: يونيو 2026
**الإصدار**: 1.0.0
