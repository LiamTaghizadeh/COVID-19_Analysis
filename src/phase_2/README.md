
# 📊 COVID-19 Data Analysis – Phase 2  
### پاکسازی داده و طراحی دیتابیس  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg)](https://www.sqlite.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-green.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🧭 نمای کلی

این مخزن حاوی **مرحله دوم** از پروژه تحلیل داده‌های جهانی کووید‑۱۹ است. در این مرحله، داده‌های خام از منابع عمومی دریافت شده، **پاکسازی** و **استانداردسازی** می‌شوند تا برای تحلیل‌های آماری آماده گردند. سپس داده‌های پاک‌شده در یک پایگاه داده **SQLite** ذخیره می‌شوند که بر اساس **قاره** تفکیک شده است تا کوئری‌نویسی و مدیریت داده‌ها تسهیل شود.

---

## 🎯 اهداف فاز دوم

- ✅ **پاکسازی داده** (Data Cleaning)  
  - حذف ستون‌های اضافی و تکراری  
  - مدیریت مقادیر گمشده (Missing Values)  
  - حذف رکوردهای نامعتبر (کشتی‌ها، جمعیت صفر)  
  - شناسایی و حذف نقاط پرت (Outliers)  
  - ایجاد متغیرهای جدید (مهندسی ویژگی)  

- ✅ **استانداردسازی** (Standardization)  
  - نرمال‌سازی داده‌های عددی برای آزمون‌های پارامتری  

- ✅ **طراحی دیتابیس** (Database Design)  
  - ایجاد پایگاه داده SQLite با جداول مجزا برای هر قاره  
  - ایندکس‌گذاری برای بهبود کارایی کوئری‌ها  

---

## 📂 ساختار پروژه

```
src/phase_2/
├── Crona_covid_19.csv               # داده‌های خام اولیه
├── clean Data.ipynb                 # نوت‌بوک پاکسازی و استانداردسازی
├── covid19_cleaned_final.csv        # خروجی داده‌های پاک‌شده
├── Design Database.ipynb            # نوت‌بوک طراحی دیتابیس و ذخیره‌سازی
├── covid19_by_continent.db          # فایل پایگاه داده SQLite
└── README.md                        # این فایل
```

---

## 🗄️ طراحی دیتابیس

پایگاه داده `covid19_by_continent.db` شامل **۷ جدول مجزا** برای هر قاره است:

| نام جدول | قاره |
|----------|------|
| `continent_asia` | آسیا |
| `continent_europe` | اروپا |
| `continent_africa` | آفریقا |
| `continent_north_america` | آمریکای شمالی |
| `continent_south_america` | آمریکای جنوبی |
| `continent_australia_oceania` | استرالیا و اقیانوسیه |
| `continent_antarctica` | جنوبگان (در صورت وجود داده) |

### 📋 ساختار هر جدول

| ستون | نوع داده | توضیحات |
|------|----------|----------|
| `active` | REAL | تعداد موارد فعال (استانداردشده) |
| `cases` | REAL | تعداد کل موارد (استانداردشده) |
| `country` | TEXT | نام کشور (کلید اصلی) |
| `critical` | REAL | تعداد موارد بحرانی (استانداردشده) |
| `deaths` | REAL | تعداد مرگ‌ومیر (استانداردشده) |
| `population` | REAL | جمعیت (استانداردشده) |
| `recovered` | REAL | تعداد بهبودیافتگان (استانداردشده) |
| `tests` | REAL | تعداد تست‌ها (استانداردشده) |
| `cfr` | REAL | نرخ مرگ‌ومیر (Case Fatality Rate) |
| `recovery_rate` | REAL | نرخ بهبودی |
| `active_rate` | REAL | نرخ موارد فعال |
| `tests_per_capita` | REAL | تعداد تست به ازای هر نفر |

> **نکته:** ستون `continent` در جداول ذخیره نمی‌شود، زیرا نام جدول خود نمایانگر قاره است.

---

## ⚙️ نحوه اجرا

### پیش‌نیازها

```bash
pip install pandas sqlite3 notebook jupyter
```

### ۱. پاکسازی داده

فایل `clean Data.ipynb` را در Jupyter باز کرده و سلول‌ها را به‌ترتیب اجرا کنید.

**خلاصه عملیات:**
- حذف ستون‌های غیرضروری (16 ستون)
- مدیریت مقادیر گمشده
- حذف نقاط پرت با روش IQR
- ایجاد متغیرهای جدید (CFR، Recovery Rate، ...)
- استانداردسازی با `StandardScaler`

**خروجی:** `covid19_cleaned_final.csv`

### ۲. طراحی دیتابیس

فایل `Design Database.ipynb` را باز کرده و اجرا کنید.

**خلاصه عملیات:**
- خواندن داده‌های پاک‌شده
- شناسایی قاره‌های منحصربه‌فرد
- ایجاد جدول مجزا برای هر قاره
- ذخیره‌سازی در SQLite

**خروجی:** `covid19_by_continent.db`

---

## 🧪 نمونه کوئری‌های تحلیلی

### دریافت ۵ کشور با بالاترین نرخ مرگ‌ومیر در آسیا

```sql
SELECT country, cfr 
FROM continent_asia 
ORDER BY cfr DESC 
LIMIT 5;
```

### میانگین نرخ بهبودی در اروپا

```sql
SELECT AVG(recovery_rate) AS avg_recovery 
FROM continent_europe;
```

### بارگیری کل داده‌های آمریکای شمالی در Pandas

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('covid19_by_continent.db')
df_na = pd.read_sql_query("SELECT * FROM continent_north_america", conn)
conn.close()
```

---

## 📊 آمار داده‌ها (پس از پاکسازی)

| ویژگی | مقدار |
|--------|--------|
| تعداد کل رکوردها | ۱۹۲ کشور |
| تعداد قاره‌ها | ۶ قاره |
| تعداد ستون‌ها (پس از پاکسازی) | ۱۳ ستون |
| حجم دیتابیس | ~ ۲ مگابایت |
| فرمت داده | استانداردشده (میانگین ۰، انحراف معیار ۱) |

---

## 🛠️ تکنولوژی‌های استفاده‌شده

<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="Pandas" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="Jupyter" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" alt="SQLite" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="Git" width="40" height="40"/>
</p>

---


## 📬 ارتباط با توسعه‌دهنده

- **نام:** اسماعیل تقی‌زاده  
- **ایمیل:** [Liam.taghizadeh@gmail.com](mailto:Liam.Taghi@gmail.com)  
- **گیت‌هاب:** [LiamTaghizadeh](https://github.com/LiamTaghizadeh)  

---

<p align="center">ساخته شده با ❤️ برای تحلیل داده‌های جهانی کووید‑۱۹</p>
```.
