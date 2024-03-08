from flask import Flask, redirect
from flask import send_from_directory,render_template, request,render_template_string
app = Flask(__name__)


todos = []
todos.append({"text": "create a todo app", "done": True})
todos.append({"text": "buy groceries", "done": True})
todos.append({"text": "take over the world", "done": False})
todos.append({"text": "start jogging every day", "done": False})
@app.route("/")
def index():    
    return render_template('index.html', todos=todos)

@app.route("/<path:name>")
def download_file(name):
    return send_from_directory("./www", name, as_attachment=False)

@app.route("/delete", methods=["GET"])
def del_todo():
    payload=request.args.get("todo")
    filtered=  list(filter(lambda t: t['text'] == payload, todos))
    if len(filtered) > 0:
        todos.remove(filtered[0])
    return render_template_string("Deleted task " + payload)

@app.route("/add", methods=["POST"])
def add_todo():
    text=request.form["todo"]
    todos.append({"text": text, "done": False})
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5004)
