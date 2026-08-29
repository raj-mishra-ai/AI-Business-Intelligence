# AI Business Intelligence Dashboard

AI Business Intelligence Dashboard is a full-stack web application for managing and analyzing company data. Users can register, log in, and perform CRUD operations on companies while viewing business insights through a clean dashboard.

## Features

- User Registration
- User Login Authentication
- JWT Token Based Authentication
- Company Management
  - Add Company
  - View Companies
  - Update Company
  - Delete Company
- Search Companies
- Filter Companies by Industry
- Dashboard Interface
- Business Report Page

## Tech Stack

### Frontend
- React.js
- React Router DOM
- Axios
- CSS

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

### Database
- SQLite

## Project Structure

```
AI-Business-Intelligence
│
├── app/
├── frontend/
│   └── my-app/
├── business_intelligence.db
├── requirements.txt
└── README.md
```

## Installation

### Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend/my-app
npm install
npm run dev
```

## API Endpoints

### Authentication

- POST /users
- POST /login

### Companies

- GET /companies
- POST /companies
- PUT /companies/{id}
- DELETE /companies/{id}

### Search & Filter

- GET /companies/search
- GET /companies/filter/industry

## Future Improvements

- Analytics Dashboard
- Charts & Graphs
- Role Based Access Control
- Export Reports
- AI-Powered Business Insights

- ## Live Demo

Frontend:
https://YOUR-VERCEL-URL.vercel.app

Backend API:
https://ai-business-intelligence-api.onrender.com

API Documentation:
https://ai-business-intelligence-api.onrender.com/docs

## Author

Raj Mishra

B.Tech CSE (2023-2027)

Shambhunath Institute of Engineering and Technology
