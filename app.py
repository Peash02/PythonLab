import datetime
from flask import Flask
app = Flask(__name__)
#<img src = "/static/Image.jpg" alt = "YOO" width = "700" height = "500">
@app.route("/")
def hello():
    return '''
    <html>
    <head>
    <title>YOO</title>
    <body>
    <h2>Yoooooooooo bro</h2>
    <p><img src = "/static/giphy.gif" alt = "vid" width = "100" height = "100"></p>
    <p><a href = "http://127.0.0.1:5000/date" target = "_self">Date</a></p>
    <p><a href = "http://127.0.0.1:5000/social" target = "_self">Social</a></p>
    <p><a href = "http://127.0.0.1:5000/factorial/10" target = "_self">Factorial</a></p>
    <p><a href = "http://127.0.0.1:5000/fibonacci/10" target = "_self">Fibonacci</a></p>
    <p><a href = "http://127.0.0.1:5000/prime/10" target = "_self">Prime</a></p>
    </body>
    </html>
    '''

todays = datetime.date.today()
today = todays.strftime("%d-%m-%Y")

@app.route("/date")
def date():
    return f"Todays Date is {today}" 

@app.route("/social")
def social():
    return '''
            <html>
            <head><title>Social</title></head>
            <body>
            <h2>Follow us on : </h2>
            <ul>
            <li><a href = "https://www.facebook.com" target = "_blank">Facebook</a></li>
            <li><a href = "https://www.instagram.com" target = "_blank">Instagram</a></li>
            <li><a href = "https://www.x.com" target = "_blank">X</a></li>
            <li><a href = "https://www.youtube.com" target = "_blank">Youtube</a></li>
            </ul>
            </body>
            </html>
            '''
            
            
@app.route("/factorial/<int:num>")
def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return f"Factorial of {num } is {fact}."

@app.route("/fibonacci/<int:lim>")
def fib(lim):
    fib = [0, 1]
    for _ in range(lim):
        fib.append(fib[-1] + fib[-2])
    return f"Fibonacci Series up to {lim} is {fib}."

@app.route("/prime/<int:num>")
def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return f"{num} is not a prime number."
            else:
                return f"{num} is a prime number."
            
        
    
    
        
if __name__ == "__main__":
    app.run(debug = True)
    



