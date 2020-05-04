pip3 install -r requirements.txt --user
python3 src/manage.py makemigrations
python3 src/manage.py migrate
# python3 manage.py collectstatic --noinput
python3 src/manage.py runserver $PORT
