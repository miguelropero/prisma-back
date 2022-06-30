from flask import Flask
from controller.bill_controller import bill
from controller.user_controller import user

app = Flask(__name__)

# Routes
app.register_blueprint(bill)
app.register_blueprint(user)

"""Documentando el mtodo"""
@app.route('/login2', methods=['POST'])
def login2():

    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    user = user_service.login(username, password)
    
    if(user):
        user.password = "*****"

    return user_schema.dump(user)



if __name__ == "__main__":
    app.run(host="0.0.0.0")

# sudo apt-get install -y python3-pip
# sudo apt install libpq-dev python3-dev
# export PATH=${PATH}:/usr/bin/python3
# python3 -m venv my_env
# source my_env/bin/activate

# pip3 install psycopg2
# pip install flask-marshmallow
# pip install flask flask-jsonpify flask-sqlalchemy flask-restful


# export FLASK_APP=bill_controller
# export FLASK_ENV=development
# flask run
