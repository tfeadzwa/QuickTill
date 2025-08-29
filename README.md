# **Point of Sale (POS) System**

Welcome to the Point of Sale (POS) system project. This repository contains the source code for a modern POS solution built with a **Flutter mobile frontend** and a **Python FastAPI backend**. The system is designed to be fast, scalable, and easy to use.

---

## **Features**

### **Frontend (Flutter)**

* Intuitive user interface for quick and easy sales transactions.
* Product management: browse and search for products by category or name.
* Cart management: add, remove, and update quantities of items in the cart.
* Receipt generation and printing.
* Offline support for continued operations without an internet connection.

### **Backend (FastAPI)**

* Secure RESTful API for all frontend-backend communication.
* User authentication and authorization (JWT-based).
* Product database management.
* Transaction processing and history logging.
* Reporting and analytics for sales data.
* Asynchronous and fast performance using FastAPI's modern Python features.

---

## **Technology Stack**

* **Frontend**: Flutter
* **Backend**: Python, FastAPI
* **Database**: PostgreSQL
* **Authentication**: JSON Web Tokens (JWT)

---

## **Getting Started**

### **Prerequisites**

* **Flutter SDK**: Ensure you have Flutter installed on your machine.
* **Python**: Version 3.8 or higher.
* **Poetry**: Recommended for Python dependency management.
* **PostgreSQL**: A running instance of a PostgreSQL database.

### **Backend Setup**

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name/backend
    ```
2.  **Install dependencies**:
    ```bash
    poetry install
    ```
3.  **Configure environment variables**:
    Create a `.env` file in the `backend` directory with your database and JWT secret configurations.
    ```
    DATABASE_URL="postgresql://user:password@host:port/dbname"
    SECRET_KEY="your-jwt-secret-key"
    ```
4.  **Run migrations**:
    ```bash
    # Command to apply database migrations (e.g., using Alembic)
    alembic upgrade head
    ```
5.  **Start the server**:
    ```bash
    poetry run uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`. You can access the auto-generated API documentation at `http://127.0.0.1:8000/docs`.

### **Frontend Setup**

1.  **Navigate to the frontend directory**:
    ```bash
    cd ../frontend
    ```
2.  **Install dependencies**:
    ```bash
    flutter pub get
    ```
3.  **Run the app**:
    ```bash
    flutter run
    ```

---

## **Contributing**

We welcome contributions! Please feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

## **License**

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
