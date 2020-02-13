#https://code.tutsplus.com/es/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

#from flask import Flask
from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL

#from werkzeug import generate_password_hash, check_password_hash
mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'victor'
app.config['MYSQL_DATABASE_PASSWORD'] = 'vvgvvg'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = '192.168.0.7'
mysql.init_app(app)


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
#            _hashed_password = generate_password_hash(_password)
            _hashed_password = _password
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
#        conn.close()


if __name__ == "__main__":
    app.run()
#    app.run(debug=True)
#    app.run(port=5002)

#ejecutar python htmlMysql
#Apunta tu navegador a http://localhost:5000/ y deberías de tener el mensaje de bienvenida.
#https://code.tutsplus.com/es/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
