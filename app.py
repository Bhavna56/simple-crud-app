from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "simple-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------- Database Models ----------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# ---------- Authentication ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # BASIC validation
        if not username or not password:
            return render_template("login.html")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # BASIC validation
        if not username or not password:
            return render_template("signup.html")

        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ---------- CRUD ----------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    items = Item.query.filter_by(user_id=session["user_id"]).all()
    return render_template("dashboard.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    title = request.form.get("title")

    # BASIC validation
    if not title:
        return redirect(url_for("dashboard"))

    item = Item(title=title, user_id=session["user_id"])
    db.session.add(item)
    db.session.commit()

    return redirect(url_for("dashboard"))


@app.route("/edit/<int:id>", methods=["POST"])
def edit_item(id):
    title = request.form.get("title")

    # BASIC validation
    if not title:
        return redirect(url_for("dashboard"))

    item = Item.query.get(id)
    item.title = title
    db.session.commit()

    return redirect(url_for("dashboard"))

@app.route("/delete/<int:id>")
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
