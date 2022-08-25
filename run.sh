echo "******* Install psycopg2 *****"
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install libpq-dev -y
sudo apt install python3-pip
pip3 install virtualenv

#sudo apt-get install python3-psycopg2 -y


if [ -f "./env" ]; then
	echo "Virtual enviroment exsists"
else
	echo "Creating virtual enviroment"
	virtualenv env
fi

echo "******* Activating Virtual Enviroment *******"
source ./env/bin/activate

pip3 install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
echo "******* Migration Done *******"
echo "******* Starting Server *******"
python manage.py runserver
