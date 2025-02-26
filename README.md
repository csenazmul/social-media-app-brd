
Django Social Media App BRD
A Django-based Social Media App BRD system with user authentication, filtering, search, pagination, and a responsive UI using TailwindCSS.

🚀 Features
1️⃣ User Management
✅ User registration, login, and logout using Django's built-in authentication system.
✅ Access control: Only authenticated users can create, edit, or delete posts.
2️⃣ Post Management
✅ Global Feed: View all users' posts with sorting & filtering options.
✅ Profile Page: View only the logged-in user’s posts.
✅ Post Creation: Users can create posts with text and optional image uploads.
✅ Edit & Delete: Only post owners can edit or delete their posts.
3️⃣ Filtering & Search
✅ Filters:
📅 Date: Show newest or oldest posts first.
🖼 Media Type: Filter by text-only or image posts.
👤 User: View posts from a specific user.
✅ Search Bar: Case-insensitive and partial-word search in post content.
✅ Optimized Search using PostgreSQL Full-Text Search (optional).
4️⃣ Pagination & Performance
✅ Paginated results (default: 10 posts per page).
✅ Django’s Paginator class for efficient pagination.
✅ TailwindCSS-based pagination UI.
5️⃣ UI/UX with TailwindCSS
✅ Responsive design with TailwindCSS.
✅ Modern login, registration, and post creation forms.
🛠️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/csenazmul/django-post-management.git
cd social-media-app-bd
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Setup Database & Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser (Admin)
bash
Copy
Edit
python manage.py createsuperuser
Enter username, email, and password.
6️⃣ Run Development Server
bash
Copy
Edit
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.
📝 Environment Variables
Create a .env file and configure your settings:

ini
Copy
Edit
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://your_db_user:your_db_password@localhost:5432/your_db_name
📁 Project Structure
csharp
Copy
Edit
django-post-management/
│── posts/                     # Main app (Post Management)
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   ├── static/                # CSS/JS assets (Tailwind)
│   ├── models.py              # Database models
│   ├── views.py               # Business logic
│   ├── urls.py                # URL routing
│── users/                     # User Authentication App
│── templates/                 # Global templates
│── static/                    # Static files
│── db.sqlite3                  # Default SQLite database (replace with PostgreSQL)
│── manage.py                   # Django project manager
│── requirements.txt             # Dependencies
│── README.md                    # Documentation
🚀 API Endpoints
Endpoint	Method	Description
/	GET	Home (Global Feed)
/profile/	GET	User's Profile Page
/post/new/	POST	Create a New Post
/post/edit/<id>/	POST	Edit a Post
/post/delete/<id>/	POST	Delete a Post
💡 Key Technologies
Django – Web framework
Django ORM – Database interactions
PostgreSQL – Database (with full-text search)
Django Paginator – Pagination
TailwindCSS – Responsive UI
Python & HTML – Backend & Frontend
🚀 Deploying to Production
1️⃣ Collect Static Files
bash
Copy
Edit
python manage.py collectstatic
2️⃣ Deploy on Heroku (Optional)
bash
Copy
Edit
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku open
📜 License
This project is open-source under the MIT License.

✅ Your Django Post Management System is Ready! 🚀
Let me know if you need any modifications! 😊