<div align="center">

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" height="60"/>
&nbsp;&nbsp;&nbsp;
<img src="https://tortoise.github.io/images/tortoise.png" alt="Tortoise ORM" height="60"/>

# FastAPI · Tortoise ORM · Aerich · JWT Auth

**A production-ready async REST API boilerplate with database migrations and secure authentication**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Tortoise ORM](https://img.shields.io/badge/Tortoise--ORM-Async-brightgreen?style=flat-square)](https://tortoise.github.io)
[![Aerich](https://img.shields.io/badge/Aerich-Migrations-blueviolet?style=flat-square)](https://github.com/tortoise/aerich)
[![JWT](https://img.shields.io/badge/Auth-JWT%20%2B%20OAuth2-orange?style=flat-square&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

---

## Overview

This project is a clean, modular boilerplate for building asynchronous REST APIs in Python. It combines the speed of **FastAPI** with the ergonomics of **Tortoise ORM** and the safety of **Aerich** schema migrations — all wired together with **JWT-based authentication** and bcrypt password hashing out of the box.

Clone it, configure it, and you have a solid foundation for your next backend project.

---

## Tech Stack

<table>
<tr>
<td align="center"><img src="https://fastapi.tiangolo.com/img/icon-white.svg" width="36"/><br/><b>FastAPI</b><br/><sub>Async web framework</sub></td>
<td align="center"><img src="https://tortoise.github.io/images/tortoise.png" width="36"/><br/><b>Tortoise ORM</b><br/><sub>Async ORM for Python</sub></td>
<td align="center"><img src="https://www.sqlite.org/images/sqlite370_banner.gif" width="60"/><br/><b>SQLite</b><br/><sub>Embedded database</sub></td>
<td align="center"><img src="https://jwt.io/img/pic_logo.svg" width="36"/><br/><b>JWT</b><br/><sub>Stateless auth tokens</sub></td>
</tr>
</table>

| Package | Version | Role |
|---|---|---|
| `fastapi` | latest | Web framework & automatic OpenAPI docs |
| `tortoise-orm` | latest | Async ORM with Pydantic integration |
| `aerich` | latest | Database migration management |
| `aiosqlite` | latest | Async SQLite driver |
| `uvicorn` | latest | ASGI server |
| `python-jose[cryptography]` | latest | JWT token encoding / decoding |
| `passlib` + `bcrypt==4.0.1` | pinned | Secure password hashing |
| `python-multipart` | latest | OAuth2 form-data parsing |
| `dotenv` | latest | Environment variable loading |

---

## Features

- ⚡ **Fully async** — every route, ORM query, and database operation is non-blocking
- 🔐 **JWT + OAuth2** — stateless bearer-token auth with refresh-ready structure
- 🔒 **bcrypt hashing** — passwords never stored in plain text
- 🗃️ **Aerich migrations** — version-controlled schema changes, no raw SQL required
- 🧩 **Repository pattern** — database logic cleanly separated from route handlers
- 🗺️ **Modular routers** — Users, Countries, Cities, Auth each in their own file
- 📄 **Auto docs** — Swagger UI and ReDoc generated automatically by FastAPI

---

## Project Structure

```
.
├── main.py                      # App entry point — registers routers & Tortoise
├── config.py                    # Tortoise ORM & Aerich configuration
├── models.py                    # Database models
├── jwt_token.py                 # JWT token creation and decoding
├── oauth2.py                    # OAuth2 dependency — extracts current user
├── pass_hashing.py              # bcrypt password utilities
├── pyproject.toml               # Aerich migration settings
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # Local SQLite database
├── migrations/
│   └── models/                  # Aerich-generated migration files
└── routes/
    ├── user_route.py
    ├── country_route.py
    ├── city_route.py
    └── authentication_route.py
```

---

## Getting Started

### Prerequisites

- Python **3.9+**
- pip

### 1. Clone the repository

```bash
git clone https://github.com/AliRaza-Dev678/FastApi_Tortoise_ORM_Aerich_Migration_Authentications.git
cd FastApi_Tortoise_ORM_Aerich_Migration_Authentications
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> **Tip:** Generate a strong secret key with `openssl rand -hex 32`

### 5. Initialize Aerich (first time only)

```bash
aerich init -t config.TORTOISE_ORM
aerich init-db
```

### 6. Apply migrations (after model changes)

```bash
aerich migrate --name "describe_your_change"
aerich upgrade
```

### 7. Start the development server

```bash
uvicorn main:app --reload
```

The API is now live at **http://127.0.0.1:8000** 🚀

---

## API Reference

### Interactive Docs

| Interface | URL |
|---|---|
| **Swagger UI** | http://127.0.0.1:8000/docs |
| **ReDoc** | http://127.0.0.1:8000/redoc |

---

### Authentication

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/auth/login` | ❌ Public | Get a JWT access token |

### Users

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/users/` | ❌ Public | Register a new user |
| `GET` | `/users/` | ✅ Required | List all users |
| `GET` | `/users/{id}` | ✅ Required | Get user by ID |

### Countries

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/countries/` | ✅ Required | Create a country |
| `GET` | `/countries/` | ❌ Public | List all countries |

### Cities

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/cities/` | ✅ Required | Create a city |
| `GET` | `/cities/` | ❌ Public | List all cities |

---

## Authentication Flow

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. POST /auth/login  →  { username, password }         │
│                                                         │
│  2. Server returns    →  { access_token,                │
│                            token_type: "bearer" }       │
│                                                         │
│  3. Client sends      →  Authorization: Bearer <token>  │
│                                                         │
│  4. Access any        →  protected route ✅             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Switching to PostgreSQL

Update the `db_url` in `config.py`:

```python
TORTOISE_ORM = {
    "connections": {
        "default": "postgres://user:password@localhost:5432/dbname"
    },
    ...
}
```

Install the async driver:

```bash
pip install asyncpg
```

Then re-run migrations:

```bash
aerich migrate --name "switch_to_postgres"
aerich upgrade
```

---

## Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch — `git checkout -b feature/your-feature`
3. Commit your changes — `git commit -m 'Add some feature'`
4. Push to the branch — `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is open-source under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ by [Ali Raza](https://github.com/AliRaza-Dev678)

[![GitHub followers](https://img.shields.io/github/followers/AliRaza-Dev678?label=Follow&style=social)](https://github.com/AliRaza-Dev678)

</div>
