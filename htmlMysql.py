#https://code.tutsplus.com/es/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

#from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()

#ejecutar python htmlMysql
#Apunta tu navegador a http://localhost:5000/ y deberías de tener el mensaje de bienvenida.
#https://code.tutsplus.com/es/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
