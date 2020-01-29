from flask import Flask
app = Flask(__name__)

todoItems = []

# test

@app.route("/add/<item>")
def addItem(item):
    todoItems.append(item)
    return "Added " + item + " to list!"

@app.route("/items")
def viewItems():
    return ", ".join(todoItems)

if __name__ == "__main__":
    app.run(debug=True)
