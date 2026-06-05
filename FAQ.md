# ❓ الأسئلة الشائعة

## التثبيت والإعداد

### س: كيف أثبت المشروع محلياً؟
ج: اتبع خطوات التثبيت في README.md. قصير:
```bash
npm install  # Backend & Frontend
pip install -r requirements.txt  # AI Service
```

### س: ما هي المنافذ المستخدمة؟
ج:
- Frontend: 3000
- Backend API: 3000/api
- AI Service: 8000
- PostgreSQL: 5432

### س: كيف أحدث قاعدة البيانات؟
ج:
```bash
psql -U postgres -d wasallni -f database/schema.sql
```

## الاستخدام

### س: كيفية التنبؤ بالطلب للمنتج؟
ج:
```bash
curl -X POST http://localhost:8000/api/forecasting/forecast \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1", "days_ahead": 7}'
```

### س: كيف أكشف السرقة أو الهدر؟
ج: النظام يكشفها تلقائياً عند تسجيل الاستهلاك.
التحقق من التنبيهات:
```bash
curl http://localhost:8000/api/anomaly/alerts/product_id
```

### س: كيف أضيف فرع جديد؟
ج:
```bash
curl -X POST http://localhost:3000/api/branches \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "الفرع الجديد", "location": "...",...}'
```

## الأداء

### س: لماذا الاستعلامات بطيئة؟
ج:
1. تحقق من الفهارس في البيانات
2. استخدم EXPLAIN ANALYZE
3. أضف Redis للـ caching
4. قسّم قاعدة البيانات إذا كبرت

### س: كيف أحسّن سرعة الـ AI Service؟
ج:
1. استخدم الـ batching
2. أضف caching للنتائج
3. قلل عدد البيانات المستخدمة
4. استخدم modelsتخفيفة (lightweight)

## الأمان

### س: كيف أحمي API من المهاجمين؟
ج:
1. استخدم HTTPS في الإنتاج
2. قعّل Rate Limiting
3. تحقق من JWT tokens
4. استخدم CORS بحذر
5. اختبر الثغرات الأمنية

### س: هل البيانات مشفرة؟
ج:
- كلمات المرور: bcrypt
- الاتصالات: HTTPS
- البيانات الحساسة: قاعدة البيانات فقط

## الصيانة

### س: كيف أعمل نسخة احتياطية؟
ج:
```bash
# يومياً
docker-compose exec postgres pg_dump -U postgres wasallni > backup-$(date +%Y%m%d).sql

# استعادة
psql -U postgres -d wasallni < backup.sql
```

### س: كيف أحديث البيانات؟
ج:
```bash
git pull origin main
docker-compose build
docker-compose up -d
```

### س: كيف أراقب الأخطاء؟
ج:
```bash
docker-compose logs -f backend
docker-compose logs -f ai
# أو استخدم Sentry/LogRocket
```

## التطوير

### س: كيف أضيف ميزة جديدة؟
ج:
1. انشئ فرع جديد: `git checkout -b feature/name`
2. اكتب الكود وادها
3. اختبر الميزة
4. انشئ Pull Request
5. راجع الكود والمرج

### س: كيف أختبر الـ APIs؟
ج:
- استخدم Postman
- استخدم curl
- اكتب اختبارات Jest/Pytest
- استخدم Thunder Client

### س: أين أضع الـ models الجديدة؟
ج:
- Backend: `src/models/`
- AI: `services/` أو `models/`
- Frontend: `src/stores/` أو `src/types/`

## التصحيح

### س: الـ API لا تعمل
ج:
1. تحقق من الخادم: `docker-compose ps`
2. اعرض السجلات: `docker-compose logs backend`
3. تحقق من قاعدة البيانات
4. أعد تشغيل الخدمات

### س: Frontend لا يتصل بـ Backend
ج:
1. تأكد من أن Backend يعمل (port 3000)
2. تحقق من CORS في Backend
3. اعرض Network Tab في المتصفح
4. تحقق من الـ URLs

### س: AI Service لا يعمل
ج:
1. تحقق من التبعيات: `pip check`
2. أعد تثبيتها: `pip install -r requirements.txt`
3. اعرض الأخطاء: `python main.py`
4. تحقق من الـ Python version

## الدعم

### س: كيف أتواصل مع الفريق؟
ج:
- GitHub Issues للمشاكل التقنية
- Email: support@wasallni.com
- Telegram: @wasallni_team

### س: هل هناك نسخة مدفوعة؟
ج: نعم، سيكون هناك نسخة Enterprise مع ميزات إضافية.

---

**آخر تحديث**: يونيو 2026
