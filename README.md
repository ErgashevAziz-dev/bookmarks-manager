# 🔖 Bookmarks Manager

A modern and simple **Bookmarks Manager** web application built with **Django, Django REST Framework, and JWT authentication**.  
Easily save, view, and manage your bookmarks with a clean REST API and beautiful Swagger documentation.

---

## ⚡ FEATURES

### 🔑 AUTHENTICATION
- User registration and login with **JWT token authentication**.
- Access and refresh tokens to secure your API.

### 📚 BOOKMARK MANAGEMENT
- Create new bookmarks with **title, URL, and description**.
- Mark bookmarks as read/unread.
- Retrieve a list of all bookmarks or a single bookmark by ID.
- Automatically linked to the authenticated user.

### 📝 API DOCUMENTATION
- Swagger UI included at `/swagger/`.
- Interactive API testing for all endpoints.

### 💾 DATABASE
- Uses **SQLite** by default (easy for development and testing).
- Can be switched to PostgreSQL if needed.

### 🚀 TECHNOLOGY STACK
- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (djangorestframework-simplejwt)
- **API Docs:** Swagger (drf-yasg)
