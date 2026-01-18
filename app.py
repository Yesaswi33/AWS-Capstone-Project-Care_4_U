from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = "dev-secret-key"

# Local in-memory storage
users = {}
appointments = []


def is_logged_in():
    return 'user_email' in session


@app.route('/')
def home():
    return render_template(
        "index.html",
        logged_in=is_logged_in()
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if email in users:
            return "User already exists"

        users[email] = {
            'name': name,
            'password': password
        }
        return redirect(url_for('login'))

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)
        if user and user['password'] == password:
            session['user_email'] = email
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


appointments = []

@app.route("/appointments", methods=["GET", "POST"])
def appointments_page():
    if request.method == "POST":
        appointment = {
            "name": request.form["fullName"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "doctor": request.form["doctor"],
            "date": request.form["date"],
            "time": request.form["time"]
        }

        appointments.append(appointment)
        return redirect(url_for("appointments_page"))

    return render_template(
        "appointments.html",
        appointments=appointments
    )


@app.route("/cancel/<int:index>")
def cancel_appointment(index):
    if 0 <= index < len(appointments):
        appointments.pop(index)

    return redirect(url_for("appointments_page"))





@app.route("/doctors")
def doctors():
    return render_template("doctors.html")


# @app.route("/doctor")
# def doctor_details():
#     return render_template("doctor_details.html")


@app.route("/doctor/sarah")
def doctor_sarah():
    return render_template("doctor_sarah.html")

@app.route("/doctor/michael")
def doctor_michael():
    return render_template("doctor_michael.html")

@app.route("/doctor/emily")
def doctor_emily():
    return render_template("doctor_emily.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@example.com" and password == "admin123":
            session["admin_logged_in"] = True
            return redirect(url_for("admin_dashboard"))

        return "Invalid admin credentials"

    return render_template("admin_login.html")



@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    return render_template("admin_dashboard.html")



if __name__ == "__main__":
    app.run(debug=True)
