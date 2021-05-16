from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '*××*'
app.config['MYSQL_PASSWORD'] = '****'
app.config['MYSQL_DB'] = '****'

mysql = MySQL(app)
@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "POST":
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
        cur.connection.commit()
        cur.execute('select * from users')
        cur.close()
        return 'successfull'
    return render_template("index.html")


@app.route('/users', methods = ["POST"])
def users():
    cur = mysql.connection.cursor()
    show = cur.execute("SELECT * FROM users")
    if show > 0:
        userDetails = cur.fetchall()
        return render_template('details.html',userDetails = userDetails)

if __name__ == '__main__':
    app.run()
