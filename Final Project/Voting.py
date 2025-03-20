from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key"
bcrypt = Bcrypt(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["voters"]
votes_collection = db["votes"]
profiles_collection = db["profiles"]

def initialize_candidates():
    candidates = ["Alice", "Bob", "Charlie"]
    for candidate in candidates:
        if not votes_collection.find_one({"name": candidate}):
            votes_collection.insert_one({"name": candidate, "votes": 0})

initialize_candidates()

@app.route('/')
def index():
    candidates = [c["name"] for c in votes_collection.find({}, {"_id": 0, "name": 1})]
    return render_template("index.html", candidates=candidates)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')  # Hash the password

        # Check if username already exists
        if not profiles_collection.find_one({"username": username}):
            profiles_collection.insert_one({"username": username, "password": hashed_password})
            session["username"] = username  # Log in the user
            return redirect(url_for("index"))
        return "Username already exists. Try another one."
    
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        user = profiles_collection.find_one({"username": username})
        if user and bcrypt.check_password_hash(user["password"], password):  
            session["username"] = username
            return redirect(url_for("index"))
        return "Invalid username or password."

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route('/vote', methods=['POST'])
def vote():
    if "username" not in session:
        return redirect(url_for("login"))
    candidate = request.form.get("candidate")
    if votes_collection.find_one({"name": candidate}):
        votes_collection.update_one({"name": candidate}, {"$inc": {"votes": 1}})
    return redirect(url_for("results"))

@app.route('/results')
def results():
    votes = {c["name"]: c["votes"] for c in votes_collection.find({}, {"_id": 0})}
    return render_template("results.html", votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
