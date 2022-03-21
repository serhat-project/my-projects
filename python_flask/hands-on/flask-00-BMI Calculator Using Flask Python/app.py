from flask import Flask, render_template, request

app=Flask(__name__)



@app.route("/", methods=["GET", "POST"])

def calculate():
    bmi=''
    if request.method== "POST":
        Weight = float(request.form.get("weight"))
        Height = float(request.form.get("height"))
        bmi=round(Weight/((Height/100)**2), 2)
    return render_template("index.html", bmi=bmi)

if __name__ == "__main__":
    app.run(debug=True)