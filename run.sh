echo "******* Activating Virtual Enviroment *******"
source env/bin/activate


python manage.py makemigrations
python manage.py migrate
echo "******* Migration Done *******"
echo "******* Starting Server *******"
python manage.py runserver
