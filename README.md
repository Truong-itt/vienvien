python -m venv .venv

.venv/Scripts/activate
pip install -r requirements.txt
django-admin startproject ptud_gk_de_1
cd ptud_gk_de_1
python manage.py startapp blog

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver


# add anh 
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/layout1/
http://127.0.0.1:8000/layout2/
http://127.0.0.1:8000/layout3/


http://127.0.0.1:8000/post/1/