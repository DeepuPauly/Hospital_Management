from flask import *
app=Flask(__name__)
app.secret_key='syam'

@app.route('/')
def welcome():
    return render_template('main.html')


@app.route('/second')
def second():
    return render_template('second.html')

app.run(debug=True)