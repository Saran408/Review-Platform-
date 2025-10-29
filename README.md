# Review Platform

A Django-based web application for managing movie and media reviews, watchlists, and user interactions.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies](#technologies)
- [License](#license)

---

## Overview
The Review Platform allows users to:
- Register and log in to the platform
- Add, edit, and delete reviews
- Create and manage personal watchlists
- View detailed information about movies and media
- Interact with other users through comments and replies

This project was developed as a Django web application with responsive templates.

---

## Features
- User authentication and profile management
- Review CRUD operations (Create, Read, Update, Delete)
- Watchlist management
- Media uploads (posters/images)
- Responsive web pages using Django templates
- Admin panel for managing content

---

## Project Structure
cinelit/ # Django project folder

cineapp/ # Django app folder

db.sqlite3 # SQLite database (ignored in GitHub)

media/ # Media files (ignored in GitHub)

docs/screenshots/ # Screenshots for README

manage.py # Django management script



## Usage

Register a new account and log in

Browse movies and shows

Add reviews and manage your watchlist

Admin users can manage all content via Django admin panel

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Saran408/Review-Platform-.git

```

2. **Navigate to the project folder**
```bash
cd cinelit
```


3. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

4.**Install dependencies**
```bash
pip install -r requirements.txt
```

5.**Apply database migrations**
```bash
python manage.py migrate
```

6.**Run the development server**
```bash
python manage.py runserver
```

7.**Open your browser at http://127.0.0.1:8000/**



## Screenshots
### Home Page
<img width="1885" height="917" alt="Home page" src="https://github.com/user-attachments/assets/60b49e31-fa5b-4325-a00a-c1e768c6ebe3" />

### Movie Page
<img width="1884" height="922" alt="Movie page" src="https://github.com/user-attachments/assets/57518f26-6df3-4f07-af1b-5edc72da7152" />


### Series Page
<img width="1912" height="920" alt="Series page" src="https://github.com/user-attachments/assets/6f6a7e13-55e2-48ec-b178-4dc6edaa0179" />



### Books Page
<img width="1905" height="914" alt="Books page" src="https://github.com/user-attachments/assets/e92e4286-99ea-4e61-8004-b91ada5a6cfc" />



### About Page
<img width="1909" height="923" alt="aboutus page" src="https://github.com/user-attachments/assets/d3fe6745-e972-4c8b-b378-60781e69bd34" />


### Contact US page
<img width="1888" height="926" alt="contactus page" src="https://github.com/user-attachments/assets/15ed600a-24da-4385-bd6a-6673a99d13ea" />


### Profile Page
<img width="1162" height="924" alt="profile page" src="https://github.com/user-attachments/assets/df5396ab-1b50-49c0-86cd-a2624fb06227" />


## Technologies

Python 3.x

Django 4.x

SQLite (development database)

HTML, CSS, Bootstrap (for templates)



## License

This project is licensed under the MIT License. See the LICENSE file for details.







