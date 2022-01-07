from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")
@app.route('/<int:num1>')
def heightchange(num1):
    number1 = int(num1/2)
    return render_template("index2.html",num1=number1)
@app.route('/<int:num1>/<int:num2>')
def widthchange(num1,num2):
    number1 = int(num1/2)
    number2=  int(num2/2)
    return render_template("index3.html",num1=number1, num2=number2)
    


# def index()
#     return

if __name__ == "__main__":
    app.run(debug=True)