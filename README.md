🚀 Bookmarks Manager
This is a simple Django + DRF project that allows users to manage bookmarks. Users can create, view, and delete bookmarks via API endpoints. JWT authentication is implemented to secure the API. Swagger UI is available for easy testing and visualization of all endpoints.

🛠️ Technologies Used

🐍 Python 3.11

🌐 Django 5.2.2

⚡ Django REST Framework

🔑 Simple JWT (Authentication)

📄 drf-yasg (Swagger documentation)

💾 SQLite (Development)

✨ Features

🔐 JWT Authentication (secure your API)

➕ Add a bookmark (POST /api/bookmarks/)

📃 View all bookmarks (GET /api/bookmarks/)

🔎 Retrieve single bookmark (GET /api/bookmarks/<id>/)

❌ Delete bookmark (DELETE /api/bookmarks/<id>/)

📊 Swagger UI: /swagger/

🚀 Usage

Obtain JWT token via POST /api/token/.

Click Authorize in Swagger UI with your token.

Access all bookmark endpoints!