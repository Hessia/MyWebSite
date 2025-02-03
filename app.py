from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("helloworld.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/about")
def aboutpage():
    return render_template("about.html")

@app.route("/grid")
def gridpage():
    return render_template("grid.html")

@app.route("/api/test")
def api_test():
    data = {"text":"hello"}
    return jsonify(data)

@app.route("/api/time")
def api_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data = {"current_time":current_time}
    return jsonify(data)
if _name_ == '_main_':
    app.run(debug=True)