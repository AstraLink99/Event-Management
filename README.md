
# Event Management

A web-based application to manage events, attendees, and tasks with a built-in calendar view and RESTful APIs. This project is designed as part of a hackathon assignment.

---

## Features

- **Event Management**:
  - Create, edit, delete, and list events.
  - View event details including attendees and task progress.
  - Integrated calendar view for visualizing events.

- **Attendee Management**:
  - Add, edit, and delete attendees.
  - Assign attendees to specific events.

- **Task Management**:
  - Create, edit, delete, and list tasks.
  - Track task status (Pending/Completed) with progress visualization.

- **Authentication**:
  - Secure login/logout functionality.
  - Protected views requiring authentication.

- **RESTful APIs**:
  - CRUD operations for events, attendees, and tasks exposed as APIs.
  - API documentation provided.

- **Responsive UI**:
  - Bootstrap styling for a clean and mobile-friendly interface.

---


## Tech Stack

- **Backend**: Django 5.1.4, Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap, FullCalendar.js
- **Database**: SQLite
- **Tools**: Git, GitHub


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AstraLink99/Event-Management.git
   cd Event-Management

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv 
   venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Login Details :
   ```bash
    username - Admin

    password - admin123

    To create a new user - python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver 




    
## API Endpoints

| **Endpoint**               | **Method** | **Description**            |
|----------------------------|------------|----------------------------|
| `/api/events/`             | GET        | List all events            |
| `/api/events/`             | POST       | Create a new event         |
| `/api/events/<id>/`        | GET        | Retrieve event details     |
| `/api/events/<id>/`        | PUT        | Update an event            |
| `/api/events/<id>/`        | DELETE     | Delete an event            |
| `/api/attendees/`          | GET        | List all attendees         |
| `/api/attendees/`          | POST       | Add a new attendee         |
| `/api/attendees/<id>/`     | GET        | Retrieve attendee details  |
| `/api/attendees/<id>/`     | PUT        | Update attendee details    |
| `/api/attendees/<id>/`     | DELETE     | Delete an attendee         |
| `/api/tasks/`              | GET        | List all tasks             |
| `/api/tasks/`              | POST       | Add a new task             |
| `/api/tasks/<id>/`         | GET        | Retrieve task details      |
| `/api/tasks/<id>/`         | PUT        | Update task details        |
| `/api/tasks/<id>/`         | DELETE     | Delete a task              |



