# 📖 دليل التطوير

## 🏗️ البنية المعمارية

### Microservices Architecture

```
Client (Browser)
    ↓
React Frontend (Port 3000)
    ↓
Node.js Backend (Port 3000/api)
├── Authentication Service
├── Order Management
├── Inventory Management
└── Analytics Aggregation
    ↓
Python AI Service (Port 8000)
├── Forecasting
├── Anomaly Detection
└── Analytics
    ↓
PostgreSQL Database
```

## 🗄️ قاعدة البيانات

### الجداول الرئيسية

#### Users
- التخزين: بيانات المستخدمين والموظفين
- المفتاح: `id` (UUID)

#### Branches
- التخزين: بيانات الفروع
- العلاقة: One-to-Many مع Users

#### Products
- التخزين: المنتجات والأصناف
- المفتاح: `id` (UUID)

#### Inventory
- التخزين: المخزون الحالي
- العلاقات: Product + Branch
- الفهرس: على `quantity` و `branch_id`

#### Orders
- التخزين: الطلبات
- الحالات: pending, confirmed, preparing, ready, delivering, delivered
- الفهرس: على `status` و `created_at`

#### Purchase Orders
- التخزين: طلبات الشراء من الموردين
- العلاقة: Supplier + Branch

#### Suppliers
- التخزين: بيانات الموردين
- المجالات: الأسعار، شروط الدفع، التقييمات

#### Inventory Logs
- التخزين: سجل تغييرات المخزون
- النوع: purchase, consumption, adjustment, waste
- الفهرس: على `branch_id` و `created_at`

## 🔐 Authentication Flow

```
1. User Login
   POST /api/auth/login {email, password}
   ↓
2. Hash Verification
   bcrypt.compare(password, hash)
   ↓
3. JWT Token Generation
   jwt.sign({id, email, role}, SECRET)
   ↓
4. Token Response
   {token, user, expiresIn}
   ↓
5. Client Storage
   localStorage.setItem('token', token)
   ↓
6. API Requests
   Authorization: Bearer {token}
```

## 🧠 AI Service Flow

### Forecasting Pipeline

```
Consumption History (30 days)
         ↓
┌─────────────────────────────┐
│  Exponential Smoothing      │ → Trend Detection
│  Polynomial Regression      │ → Pattern Recognition
│  ARIMA-like Model           │ → Seasonality
└─────────────────────────────┘
         ↓
┌─────────────────────────────┐
│  Weighted Ensemble          │
│  0.4 * ES + 0.35 * PR + ... │ → Combined Forecast
└─────────────────────────────┘
         ↓
┌─────────────────────────────┐
│  Confidence Calculation     │
│  Based on Model Agreement   │
└─────────────────────────────┘
         ↓
Forecasts (7 days) + Confidence + Recommendations
```

### Anomaly Detection Pipeline

```
Consumption Data
         ↓
┌─────────────────────────────┐
│  Statistical Analysis       │
│  - Z-Score Check           │
│  - Mean/Std Deviation      │
└─────────────────────────────┘
         ↓
┌─────────────────────────────┐
│  ML-based Detection         │
│  - Isolation Forest         │
│  - Seasonal Anomaly         │
└─────────────────────────────┘
         ↓
Anomaly Report + Severity + Recommendations
```

## 📋 نماذج البيانات (Pydantic)

### ForecastRequest
```python
{
  "product_id": "string",
  "days_ahead": 7
}
```

### ForecastResponse
```python
{
  "date": "2026-06-05",
  "predicted_demand": 12.5,
  "confidence": 0.85,
  "recommendation": "string"
}
```

### AnomalyDetectionRequest
```python
{
  "actual_consumption": 50.0,
  "expected_consumption": 10.0,
  "product_id": "string"
}
```

## 🔄 State Management (Zustand)

### Auth Store
```typescript
- user: User | null
- token: string | null
- isAuthenticated: boolean
- login(email, password): Promise
- logout(): void
```

### Order Store
```typescript
- orders: Order[]
- loading: boolean
- fetchOrders(): Promise
- createOrder(data): Promise
- updateOrderStatus(id, status): Promise
```

### Inventory Store
```typescript
- items: InventoryItem[]
- lowStockItems: InventoryItem[]
- fetchItems(): Promise
- updateQuantity(id, quantity, type): Promise
```

## 🔌 API Response Format

### Success Response
```json
{
  "success": true,
  "data": { ... },
  "message": "optional message"
}
```

### Error Response
```json
{
  "success": false,
  "error": "error message",
  "code": "ERROR_CODE"
}
```

## 📊 مؤشرات الأداء (KPIs)

### البيع
- Total Sales
- Orders Count
- Average Order Value
- Daily/Weekly/Monthly Trends

### المخزون
- Stock Levels
- Turnover Rate
- Waste Percentage
- Low Stock Alerts

### الفروع
- Branch Revenue
- Customer Rating
- Delivery Time
- Order Success Rate

### الأرباح
- Gross Profit
- Net Profit
- Profit Margin
- Cost per Order

## 🔄 Workflow Examples

### إنشاء طلب
```
1. Frontend: POST /api/orders
2. Backend: Validate data, Save to DB
3. AI Service: Update consumption expectations
4. Inventory: Deduct items from stock
5. Response: Order confirmation
```

### كشف الشذوذ
```
1. Inventory Log: Record consumption
2. AI Service: Compare with expected
3. Detection: If anomaly detected
4. Alert: Notify manager
5. Log: Store alert in database
```

### التنبؤ بالطلب
```
1. Daily: Collect consumption data
2. AI Service: Run forecasting models
3. Analysis: Calculate ensemble forecast
4. Recommendations: Generate purchase suggestions
5. Notification: Alert managers
```

## 🚀 Deployment

### Docker Compose
```yaml
version: '3.8'
services:
  postgres:
    image: postgres:12
    environment:
      POSTGRES_DB: wasallni
      POSTGRES_PASSWORD: password
    
  backend:
    build: ./wasallni-backend
    ports:
      - "3000:3000"
    depends_on:
      - postgres
    
  ai:
    build: ./wasallni-ai
    ports:
      - "8000:8000"
    
  frontend:
    build: ./wasallni-frontend
    ports:
      - "80:3000"
```

## 🧪 اختبار الـ APIs

### باستخدام curl
```bash
# Login
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@wasallni.com", "password": "password"}'

# Get Orders
curl http://localhost:3000/api/orders \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### باستخدام Postman
1. Import المشروع
2. Set environment variables
3. Run requests

## 📚 مراجع إضافية

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Express.js Guide](https://expressjs.com/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Manual](https://www.postgresql.org/docs/)
- [Scikit-learn](https://scikit-learn.org/)

---

**آخر تحديث**: يونيو 2026
