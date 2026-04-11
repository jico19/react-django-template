# React-Django Template

A minimal starter template combining Django REST Framework and React with Simple JWT authentication.

---

## 🚀 Getting Started

### 1. Backend

```bash
cd backend/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 2. Frontend

```bash
cd frontend/
npm install
npm run dev
```

Once running:
- **Backend** → http://127.0.0.1:8000/
- **Frontend** → http://localhost:5173/

---

## 📁 Project Structure

```
project-root/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   └── app/
└── frontend/
    ├── package.json
    └── src/
```

---

## 📝 Notes

- Auth is handled via **Simple JWT** (access + refresh tokens).
- Default database is **SQLite** — change it in `settings.py` when needed.
- Create a **`.env` file** for sensitive keys (e.g. `SECRET_KEY`, `DB_*`) and make sure it's in `.gitignore`.
- Static and media files are already excluded from version control.
