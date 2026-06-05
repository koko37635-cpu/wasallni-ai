# 🚀 دليل النشر والإطلاق

## المتطلبات

- Docker و Docker Compose
- Server Linux (Ubuntu 20.04+)
- Domain name
- SSL Certificate

## خطوات النشر

### 1. إعداد السيرفر

```bash
# تحديث النظام
sudo apt-get update
sudo apt-get upgrade -y

# تثبيت Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# تثبيت Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.0.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# إنشاء مجلد المشروع
mkdir ~/wasallni && cd ~/wasallni
```

### 2. نسخ الملفات

```bash
git clone https://github.com/yourusername/wasallni.git .
cd wasallni
```

### 3. إعداد متغيرات البيئة

```bash
# Backend
cd wasallni-backend
cp .env.example .env
# عدّل .env

# AI Service
cd ../wasallni-ai
cp .env.example .env
# عدّل .env

cd ..
```

### 4. بناء صور Docker

```bash
docker-compose build
```

### 5. تشغيل الخدمات

```bash
docker-compose up -d
```

### 6. إعداد قاعدة البيانات

```bash
# الدخول لـ PostgreSQL
docker-compose exec postgres psql -U postgres

# إنشاء قاعدة البيانات
CREATE DATABASE wasallni;
\c wasallni

# تشغيل Schema
\i /database/schema.sql
\i /database/seed.sql

# الخروج
\q
```

### 7. التحقق من الحالة

```bash
# عرض السجلات
docker-compose logs -f

# فحص الخدمات
curl http://localhost:3000/api/health
curl http://localhost:8000/health
```

## إعدادات الإنتاج

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name wasallni.com www.wasallni.com;

    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name wasallni.com www.wasallni.com;

    # SSL Certificates
    ssl_certificate /etc/letsencrypt/live/wasallni.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wasallni.com/privkey.pem;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Backend API
    location /api/ {
        proxy_pass http://localhost:3000/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # AI Service
    location /ai/ {
        proxy_pass http://localhost:8000/;
        proxy_set_header Host $host;
    }
}
```

### SSL Certificate

```bash
# استخدام Let's Encrypt
sudo apt-get install certbot python3-certbot-nginx

sudo certbot certonly --nginx -d wasallni.com -d www.wasallni.com
```

## المراقبة والصيانة

### عرض السجلات

```bash
# جميع الخدمات
docker-compose logs -f

# خدمة محددة
docker-compose logs -f backend
docker-compose logs -f ai
```

### النسخ الاحتياطي

```bash
# النسخ من قاعدة البيانات
docker-compose exec postgres pg_dump -U postgres wasallni > backup.sql

# استعادة البيانات
docker-compose exec postgres psql -U postgres wasallni < backup.sql
```

### التحديثات

```bash
# سحب أحدث الكود
git pull origin main

# إعادة بناء الصور
docker-compose build

# إعادة تشغيل الخدمات
docker-compose up -d
```

## التعامل مع المشاكل

### إذا لم تتصل الخدمات

```bash
# تحقق من الحالة
docker-compose ps

# أعد تشغيل الخدمات
docker-compose restart

# عرض الأخطاء
docker-compose logs backend
docker-compose logs ai
```

### مشاكل قاعدة البيانات

```bash
# تحقق من الاتصال
docker-compose exec backend npm run db:test

# أعد تشغيل PostgreSQL
docker-compose restart postgres
```

## أداء التحسين

### Redis Caching

```bash
docker-compose ps
# إضافة Redis لـ caching
```

### Database Optimization

```sql
-- تحليل الاستعلامات البطيئة
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending';

-- إنشاء فهارس إضافية
CREATE INDEX idx_orders_branch_status ON orders(branch_id, status);
```

---

**آخر تحديث**: يونيو 2026
