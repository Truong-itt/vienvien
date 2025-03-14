python -m venv .venv

.venv/Scripts/activate
pip install -r requirements.txt
django-admin startproject ptud_gk_de_1
cd ptud_gk_de_1
python manage.py startapp blog

python manage.py makemigrations
python manage.py migrate
