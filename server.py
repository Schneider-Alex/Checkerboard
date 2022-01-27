from flask import Flask, render_template
app = Flask(__name__)

# main issue is that integers must be even due to for loop structure on HTML page, 
# ideally would redo and create  a foorloop that can accept odd numbers


@app.route('/')
def welcome():
    return render_template("index.html",num1=8,num2=8,color1='red',color2='black')

@app.route('/<int:num1>')
def heightchange(num1):
    number1 = int(num1/2)
    return render_template("index.html",num1=number1,num2=number1,color1='red',color2='black')


@app.route('/<int:num1>/<int:num2>')
def widthchange(num1,num2):
    number1 = int(num1/2)
    number2=  int(num2/2)
    return render_template("index.html",num1=number1, num2=number2,color1='red',color2='black')
    

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def colorchange(num1,num2,color1,color2):
    number1 = int(num1/2)
    number2 = int(num2/2)
    return render_template("index.html",num1=number1, num2=number2,color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)