from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_World():
    print ('Hey')
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    MTK_ID = request.form.get ('MTK_ID')
    print (MTK_ID)
    print ('HEYYYYYYYY')

if __name__ == '_main_':
    app.run()