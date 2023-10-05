from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_geek():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)