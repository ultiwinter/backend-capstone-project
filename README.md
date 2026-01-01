# Little Lemon Restaurant – Backend Portfolio Project

This repository contains the backend implementation for **Little Lemon Restaurant**, a portfolio project developed as part of the Meta Backend Developer Professional Certificare. The project demonstrates clean backend architecture using **Django** and **Django REST Framework (DRF)**, combining server-rendered pages with secure RESTful APIs.

---

## Project Overview

Little Lemon is a fictional, family-owned Mediterranean restaurant. This project provides:

- A server-rendered website (Home, Menu, Booking, About)
- Secure REST APIs for menu and table bookings
- Token-based authentication
- Clean separation between frontend templates and backend APIs

The project is designed to showcase **real-world backend development practices** suitable for a professional portfolio.

---

## Tech Stack

- **Python 3.12**
- **Django 6.0**
- **Django REST Framework**
- **SQLite / MySQL (configurable)**
- **HTML5 / CSS3**
- **Token-based Authentication**

---

## Project Structure

```
littlelemon/
│
├── restaurant/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   └── img/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── menu.html
│   │   ├── booking.html
│   │   └── about.html
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── manage.py
└── requirements.txt
```

---

## Website Pages

| Page | Description |
|----|----|
| Home | Landing page with promotional content |
| Menu | Displays restaurant menu items |
| Booking | Placeholder for table reservation |
| About | Restaurant information |

All pages are rendered using Django templates and share a common layout via `base.html`.

---

## API Features

### Authentication
- Token-based authentication using DRF
- Secure endpoints protected with `IsAuthenticated`

### Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/api-token-auth/` | Obtain auth token |
| GET | `/menu/` | List menu items |
| POST | `/menu/` | Create menu item |
| GET | `/menu/<id>/` | Retrieve menu item |
| PUT | `/menu/<id>/` | Update menu item |
| DELETE | `/menu/<id>/` | Delete menu item |

---

## Testing & API Usage with Insomnia

- Django unit tests supported via `manage.py test`
- API endpoints testable using **Insomnia** or **Postman**

### 1. Obtain Authentication Token

- Method: **POST**  
- URL: `http://127.0.0.1:8000/api-token-auth/`
- Body type: **JSON**
```json
{
  "username": "reviewer",
  "password": "thisisapassword1"
}
```
- Response:
```json
{
  "token": "your_token_here"
}
```
Save the returned token for subsequent requests.

### 2. Make an Authenticated GET Request (Retrieve Menu Item)

- Method: **GET**  
- URL: `http://127.0.0.1:8000/restaurant/menu/1`
- In **Auth** tab:
  - Auth Type: **Bearer Token**
  - Token: `{your_token}`
  - Prefix: `Token`

### 3. Make an Authenticated POST Request (Create Menu Item)

- Method: **POST**  
- URL: `http://127.0.0.1:8000/restaurant/menu/`
- In **Auth** tab:
  - Auth Type: **Bearer Token**
  - Token: `{your_token}`
  - Prefix: `Token`
- In **Body** tab:
  - Body Type: **Form**
  - Fields:
    ```
    title = {add_menu_item_title}
    price = {add_menu_item_price}
    inventory = {add_menu_item_inventory}
    ```

---

## Testing

- Django unit tests supported via `python manage.py test`
- API endpoints testable using **Insomnia**

---

## ⚙️ Setup Instructions

You can set up the project using either **Pipenv (recommended)** or a traditional virtual environment.

---

### Option A: Setup Using Pipenv (Recommended)

Pipenv provides dependency management and virtual environment handling in one tool.

#### 1. Install Pipenv (if not already installed)
```bash
pip install pipenv
```

#### 2. Clone the repository
```bash
git clone https://github.com/your-username/little-lemon-backend.git
cd little-lemon-backend
```

#### 3. Install dependencies using Pipenv
```bash
pipenv install
```

#### 4. Activate the Pipenv shell
```bash
pipenv shell
```

#### 5. Run migrations
```bash
python manage.py migrate
```

#### 6. Create superuser
```bash
python manage.py createsuperuser
```

#### 7. Run development server
```bash
python manage.py runserver
```

---

## Design Decisions

- Separation of **HTML views** and **API endpoints**
- Reusable template layout using `base.html`
- Strict URL naming to prevent routing errors
- Secure APIs with token authentication
- Scalable structure suitable for future frontend frameworks

---

## Future Improvements

- Connect booking page to live booking API
- Add Django Forms for reservations
- Add role-based permissions
- Add pagination and filtering to Menu API
- Frontend integration with React or Vue

---

## Author

**Ahmed Sheta**  
AI Software Engineer | Backend & Data Engineering Background

This project is part of my professional portfolio and demonstrates my ability to design, secure, and structure backend systems using Django and DRF.

---

## License

This project is for educational and portfolio purposes via Apache 2.0 License.

