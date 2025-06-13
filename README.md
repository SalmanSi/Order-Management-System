# 🛒 Order Management System

A Flask-based web application for managing customer orders with user authentication, CRUD operations, and comprehensive activity logging.

---

## 🚀 Features

- 🔐 **User Authentication** - Secure login/logout with Flask-Login
- 📦 **Order Management** - Create, read, update, and delete customer orders
- ✅ **Order Status Tracking** - Mark orders as delivered
- 📜 **Activity Logging** - Complete audit trail of all user actions
- 💾 **Data Persistence** - SQLite database with SQLAlchemy ORM
- 🎨 **Clean Interface** - Responsive web UI with intuitive navigation

---

## 🏗️ System Architecture

### **Authentication System**
- Session-based authentication using Flask-Login
- User registration and login with password hashing
- Protected routes requiring authentication
- Automatic redirection to login for unauthorized access

### **CRUD Operations**
- **Create**: Add new orders with unique order IDs
- **Read**: View all orders for authenticated users
- **Update**: Edit order details (order ID is immutable after creation)
- **Delete**: Remove orders with proper logging

### **Logging System**
- Tracks all user actions (Create, Edit, Delete, Mark Delivered)
- Stores both database references and string identifiers
- Maintains log integrity even after order deletion
- Provides complete audit trail for compliance

### **Forms & Validation**
- **OrderForm**: Complete order creation with validation
- **EditOrderForm**: Restricted editing (prevents order ID changes)
- **LoginForm/SignupForm**: User authentication forms
- Server-side validation with WTForms

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Forms**: WTForms with CSRF protection
- **Templates**: Jinja2 templating engine
- **Frontend**: HTML5 with responsive design

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git cloen https://github.com/SalmanSi/Order-Management-System.git
cd order-management-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```python
flask shell
>>> from models import db
>>> db.create_all()
>>> exit()
```

### 5. Run Application
```bash
python app.py
```
Visit: http://127.0.0.1:5000

---

## 🏛️ Database Schema

### User Model
- User authentication and session management
- One-to-many relationship with orders

### Order Model
- Core business entity with immutable order IDs
- Tracks order status and delivery information
- Linked to user who created the order

### Log Model
- Independent audit trail system
- Stores both database IDs and string identifiers
- Maintains data integrity across order lifecycle

---

## 🔧 Key Technical Solutions

### **Order ID Immutability**
- Separate forms for creation vs. editing
- Prevents accidental changes to order identifiers
- Maintains referential integrity in logs

### **Log Persistence**
- Dual storage approach (DB ID + string ID)
- Survives order deletion operations

### **Authentication Flow**
- Session-based user management
- Route protection with decorators
- Secure password handling with hashing

---

## 📋 Usage

1. **Register/Login** - Create account or sign in
2. **Create Orders** - Add new customer orders with unique IDs
3. **Manage Orders** - Edit details, mark as delivered, or delete
4. **View Logs** - Monitor all system activity and changes
5. **Secure Logout** - End session safely
