# Little Lemon Restaurant – Backend Portfolio Project

This repository contains the backend implementation for **Little Lemon Restaurant**, a portfolio project developed as part of the Meta Backend Developer curriculum. The project demonstrates clean backend architecture using **Django** and **Django REST Framework (DRF)**, combining server-rendered pages with secure RESTful APIs.

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

## Testing

- Django unit tests supported via `python manage.py test`
- API endpoints testable using **Insomnia** or **Postman**

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/little-lemon-backend.git
cd little-lemon-backend
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run development server
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

