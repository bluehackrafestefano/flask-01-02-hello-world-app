from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World I am Rafe!</p>"

@app.route("/my_page")
def my_page():
    return "<p>Hello, World this is my page!</p>"

@app.route("/my_template")
def my_template():
    name = 'Paolo'
    return render_template('my_template.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=80)
