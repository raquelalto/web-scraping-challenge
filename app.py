from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def index():
    # variable = "text"
    # variable2 = "text2"
    return render_template("index.html")

# @app.rout("/2ndhtml")
# def 2ndhtml():
#     canaddvariable = "text"
#     return render_template("2ndhtnl.html", variable=variable, variable2=variable2)



    if __name__=="__main__":
        app.run(debug=True)