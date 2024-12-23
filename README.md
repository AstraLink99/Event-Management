Installation :

1. Clone the repository / download the ZIP file
   git clone https://github.com/AstraLink99/Event-Management.git
   cd Event-Management
   
2. Create and activate a virtual environment:
   python -m venv venv -> creation
   venv\Scripts\activate -> activation

3. Install dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Login Details :
   username - Admin
   password - admin123

   To create a new user - python manage.py createsuperuser

6. Run the development server: (http://127.0.0.1:8000/)
   python manage.py runserver
  
