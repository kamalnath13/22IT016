from flask import Flask 
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello,world!'
@app.route('/getdetails')
def get_details():
    return 'Kamalnath - 22it016'
if__name__ == '__main__':
    app.run(debug=True)