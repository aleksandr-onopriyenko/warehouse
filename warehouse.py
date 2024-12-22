from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Define a model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Create database tables (run once)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add_item():
    name = request.form.get("name")
    if name:
        new_item = Item(name=name)
        db.session.add(new_item)
        db.session.commit()
    return "Item added!"


if __name__ == "__main__":
    pass
