from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    rasp = request.form["rasp"]
    straw = request.form["straw"]
    apple = request.form["apple"]
    total = int(rasp) + int(straw) + int(apple)
    first = request.form["first_name"]
    last = request.form["last_name"]
    student = request.form["student_id"]
    return render_template("checkout.html", first_name=first, last_name=last, student_id=student, apple=apple, rasp=rasp, straw=straw, total=total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    