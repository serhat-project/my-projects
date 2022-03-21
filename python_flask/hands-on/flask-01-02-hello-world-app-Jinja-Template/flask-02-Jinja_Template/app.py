from flask import Flask, render_template

app = Flask(__name__)


@app.route("/yavuz")
def head():
    return render_template("index.html", number1 = 34, number2 = 45)




if __name__=="__main__":
    app.run(debug=True)