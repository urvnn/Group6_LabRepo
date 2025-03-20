from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import FileSystemLoader
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Allow Flask to load templates from both 'HTML Template' and 'templates' folders
app.jinja_loader = FileSystemLoader(["HTML Template", "templates"])

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["voters"]
candidates_collection = db["candidates"]
votes_collection = db["votes"]
profiles_collection = db["profiles"]

# Admin Credentials (Stored in DB instead of hardcoding)
ADMIN_USERNAME = "admin"

@app.route('/')
def index():
    candidates = [c["name"] for c in candidates_collection.find({}, {"_id": 0, "name": 1})]
    return render_template("index.html", candidates=candidates)

@app.route('/admin')
def admin():
    if "admin" not in session:
        return redirect(url_for("admin_login"))
    candidates = list(candidates_collection.find({}, {"_id": 0, "name": 1, "party": 1, "bio": 1}))  # Include party and bio
    return render_template("admin.html", candidates=candidates)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = profiles_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password) and username == ADMIN_USERNAME:
            session["admin"] = True
            return redirect(url_for("admin"))
        return "Invalid admin credentials. Try again."
    return render_template("admin_login.html")

@app.route('/admin/logout')
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("index"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if not profiles_collection.find_one({"username": username}):
            hashed_password = generate_password_hash(password)
            profiles_collection.insert_one({"username": username, "password": hashed_password})
            session["username"] = username
            return redirect(url_for("index"))
        return "Username already exists. Try another one."
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = profiles_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            session["username"] = username
            return redirect(url_for("index"))
        return "Invalid credentials. Try again."
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route('/admin/add_candidate', methods=['POST'])
def add_candidate():
    if "admin" not in session:
        return redirect(url_for("admin_login"))
    name = request.form.get("name")
    party = request.form.get("party")
    bio = request.form.get("bio")
    if name and party and bio:
        candidates_collection.insert_one({"name": name, "party": party, "bio": bio, "votes": 0})
    return redirect(url_for("admin"))

@app.route('/admin/remove_candidate', methods=['POST'])
def remove_candidate():
    if "admin" not in session:
        return redirect(url_for("admin_login"))
    candidate_name = request.form.get("candidate_name")
    if candidate_name:
        candidates_collection.delete_one({"name": candidate_name})
        votes_collection.delete_many({"candidate": candidate_name})  # Remove all votes for the candidate
    return redirect(url_for("admin"))

@app.route('/vote', methods=['POST'])
def vote():
    if "username" not in session:
        return redirect(url_for("login"))
    
    username = session["username"]
    existing_vote = votes_collection.find_one({"user": username})

    if existing_vote:
        return redirect(url_for("already_voted"))  # Redirect to the already voted page

    candidate = request.form.get("candidate")
    candidate_doc = candidates_collection.find_one({"name": candidate})

    if candidate_doc:
        votes_collection.insert_one({"user": username, "candidate": candidate_doc["name"]})

    return redirect(url_for("confirmation"))  # Ensure this points to the correct route

@app.route('/confirmation')
def confirmation():
    return render_template("confirmation.html")


@app.route('/already_voted')
def already_voted():
    return render_template("already_voted.html")

@app.route('/results')
def results():
    vote_counts = votes_collection.aggregate([
        {"$group": {"_id": "$candidate", "votes": {"$sum": 1}}}
    ])
    votes = {v["_id"]: v["votes"] for v in vote_counts}
    return render_template("results.html", votes=votes)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
