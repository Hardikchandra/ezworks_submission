Secure File Sharing System (Backend)

A secure file-sharing backend built with ⚡ FastAPI, 🐘 PostgreSQL, and 🐳 Docker — designed for uploading, sharing, and downloading documents through encrypted, time-limited links.


🚀 Features

🧑‍💼 Role-based access control: Ops (upload) & Client (download)

✅ Email verification for new users

📄 File support: Upload .docx, .pptx, and .xlsx only

🔐 Secure, time-limited download links (JWT)

🗃️ File validation & storage

🐳 Dockerized setup with PostgreSQL & FastAPI

📬 Postman collection included for testing

✨ Auto-generated Swagger docs: http://localhost:8000/docs


🧰 Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| FastAPI    | Web framework (async, fast) |
| SQLAlchemy | ORM for PostgreSQL          |
| PostgreSQL | Relational DB               |
| Docker     | Containerization            |
| Uvicorn    | ASGI Server                 |
| JWT (Jose) | Secure token encoding       |
| Passlib    | Password hashing (bcrypt)   |


🏁 Deployment Status
✅ This project is ready for production deployment.
✅ The most important step — Dockerizing the application — has been completed.
By containerizing both the FastAPI backend and PostgreSQL database with Docker Compose, we’ve ensured consistent, reliable behavior across development, staging, and production environments.



⚙️ Prerequisites
✅ Docker Desktop (Required) → https://www.docker.com/products/docker-desktop

✅ Python 3.10+ (For optional venv setup)

✅ Git




🧑‍💻 Local Setup Instructions
🚨 Step 1: Clone the repository

git clone https://github.com/Hardikchandra/ezworks_submission
cd sezworks_submission
📝 Step 2: Create a .env file

DATABASE_URL=postgresql://postgres:password@db:5432/fileshare
SECRET_KEY=your_very_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30



🐳 Option 1: Docker Setup (Recommended)
Start everything using Docker Compose:

docker-compose up --build
✅ Visit: http://localhost:8000/docs

🐍 Option 2: Manual Setup (Using venv)
Create and activate virtual environment:

python3 -m venv venv
source venv/bin/activate

Install Python dependencies:
pip install -r requirements.txt

Start only the PostgreSQL container:

docker-compose up db
Run FastAPI server:
uvicorn app.main:app --reload


📬 Postman Collection
Import this file into Postman:
SecureFileSharing.postman_collection.json

Test Flow:
➕ POST /client/signup

✅ GET /client/verify-email/{id}

📤 POST /ops/upload

🔗 GET /client/download-file/{file_id}

📥 GET /client/secure-download/{token}


🔐 Access Rules

| Role   | Upload | Download | Generate Link | Verify Email |
| ------ | ------ | -------- | ------------- | ------------ |
| Ops    | ✅     | ❌        | ❌            | ❌           |
| Client | ❌     | ✅        | ✅            | ✅           |


Download links are time-limited JWTs tied to the Client

Unauthorized access = 403 Forbidden

🧪 Sample DB Setup
Manually update users via psql:

docker exec -it file_sharing-db-1 psql -U postgres -d fileshare

In the PostgreSQL prompt:

UPDATE users SET is_verified = true WHERE id = 3;
UPDATE users SET is_ops = true WHERE id = 1;

📂 API Summary
POST /client/signup → Register new client

GET /client/verify-email/{user_id} → Mark verified

POST /ops/upload → Upload file (ops only)

GET /client/download-file/{file_id} → Get secure token URL

GET /client/secure-download/{token} → Download file (client-only)



🧪 Common Commands

| Task              | Command                                |
| ----------------- | -------------------------------------- |
| Start App         | docker-compose up --build              |
| Stop Containers   | docker-compose down                    |
| Tail Backend Logs | docker logs -f file\_sharing-backend-1 |
| Rebuild All       | docker-compose build --no-cache        |


Why Docker?

✅ Eliminates “it works on my machine” issues

✅ Bundles the FastAPI app, Python dependencies, and environment variables

✅ Allows you to run the same code locally, on a server, or in the cloud

✅ Works well with CI/CD platforms like GitHub Actions, Railway, or Render

Docker Makes It Easy to:
1. Package your app (code + dependencies + config)
2. Run anywhere (local, cloud, staging, production)
3. Scale predictably

Save hours in setup and debugging



☁️ One-Click Deployment Options

You can also deploy this to PaaS platforms like:

Railway.app (Dockerfile supported)

Render.com (via Dockerfile)

Fly.io (supports volume and multi-container apps)

GitHub Codespaces or Codesphere (for internal dev testing)


✅ Future Enhancements

🔐 Login & JWT session flow

⏱ Expiring token validation in middleware

🧾 Download tracking per user

☁️ Deploy to Render / Railway / Fly.io

👋 Author
Made with ❤️ by Hardik Chandra
For the Back-End Intern Test Challenge at Ez Works
