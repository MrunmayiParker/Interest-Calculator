from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/interest", methods=['POST', 'GET'])

def calc():
    interest = ''
    total = ''

    if request.method == 'POST' :
        principal = float(request.form.get("principal"))
        interestrate = float(request.form.get("interestrate"))
        term = float(request.form.get("term"))

        interest = (principal* interestrate * term)/100.0

        total = principal + interest
    return render_template("interest.html", total=total)