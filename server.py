from flask import Flask
app = Flask(__name__)


# routes = ['/', '/dojo', '/say/<string:name>', '/repeat/<int:count>/<string:expression>']
# if @app.rount() not in routes 

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_who(name):
    # print('*'*5 + name + '*'*5)
    return f'Hi {name}!'

@app.route('/repeat/<int:count>/<string:expression>')
def repeat_expression(count, expression):
    x = expression
    cntLoop = 1
    while count > 1:
        x += f' {expression}'
        count -= 1
        cntLoop += 1
    print('*'*5 + str(cntLoop) + '*'*5)
    return x

@app.errorhandler(404)
def error404(error):
    return '<h1>Sorry! No response. Try again.</h1>', 404

# Turn debug function on
if __name__ == "__main__":
    app.run(debug=True)
