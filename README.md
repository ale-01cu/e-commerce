# E-commerce Platform

This is a full-stack e-commerce platform featuring a Django REST Framework backend and a React frontend. It includes a comprehensive set of features for a modern online store, from user authentication to a product recommendation system.

## Features

- **User Authentication**: Secure user registration, login, and account activation using Djoser and JSON Web Tokens (JWT).
- **Product Catalog**: Manage products, categories, brands, images, and units of measure.
- **Shopping Cart**: Full-featured shopping cart with operations to add, update, remove, and clear items.
- **Order Management**: System for placing and tracking customer orders.
- **Reviews and Ratings**: Allows users to leave comments and ratings on products.
- **Product Offers**: Functionality to create and manage special offers and discounts.
- **Search Engine**: A search system to help users find products easily.
- **User Profiles**: User profiles with personal information, photos, and addresses.
- **Product Recommendation System**: A content-based recommendation engine to suggest related products to users.
- **User History**: Tracks products viewed by users.

## Technology Stack

- **Backend**:
  - Python 3.11
  - Django & Django REST Framework
  - PostgreSQL (for production), SQLite (for development)
  - Djoser for authentication
  - Simple JWT for JSON Web Token handling
  - NLTK, Scikit-learn, and Pandas for the recommendation system

- **Frontend**:
  - React
  - Redux for state management
  - Vite for the build tool
  - Axios for API requests
  - Formik and Yup for form handling and validation

- **Deployment**:
  - Docker

---

## Backend Setup

### Prerequisites

- Python 3.11
- `pip`
- `virtualenv`

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd e-commerce
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    # For Windows
    pip install virtualenv
    virtualenv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt 
    # Note: You might need to create a requirements.txt file using pip freeze > requirements.txt
    ```

4.  **Set up environment variables**:
    Create a `.env` file in the root of the backend project and add the following variables. Fill them with your own settings.

    ```env
    SECRET_KEY=your_secret_key
    ENVIRONMENT=dev

    DOMAIN=localhost
    PORT=8000

    DATABASE_URL=your_database_url
    DATABASE_PORT=your_database_port
    DATABASE_NAME=your_database_name
    DATABASE_USER=your_database_user
    DATABASE_PASSWORD=your_database_password

    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    DEFAULT_FROM_EMAIL=your_email
    EMAIL_HOST=your_email_host
    EMAIL_HOST_USER=your_email_host_user
    EMAIL_HOST_PASSWORD=your_email_host_password
    EMAIL_PORT=your_email_port
    EMAIL_USE_TLS=True
    ```

5.  **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

6.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```
    The backend will be available at `http://localhost:8000`.

---

## Frontend Setup

### Prerequisites

- Node.js
- `npm` or `yarn`

### Installation

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    # or
    yarn install
    ```

3.  **Run the development server**:
    ```bash
    npm run dev
    # or
    yarn dev
    ```
    The frontend will be available at `http://localhost:5173` or another port specified by Vite.

---

## API Documentation

The API documentation is available at the `/docs/` endpoint when the backend server is running (e.g., `http://localhost:8000/docs/`).