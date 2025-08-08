from flask import Flask, render_template
import subprocess
import os
import random
import sys

app = Flask(__name__)

# Detect OS
WINDOWS = os.name == 'nt'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/wave")
def wave():
    gesture_script = os.path.join(os.getcwd(), "gesture_control.py")

    if WINDOWS:
        subprocess.Popen(["start", "cmd", "/k", f"python {gesture_script}"], shell=True)
    else:
        subprocess.Popen(["python3", gesture_script])

    return render_template(
        "running.html",
        title="Gesture Control Running",
        emoji="🖐",
        message="Gesture Control Running..."
    )

@app.route("/type_scream")
def type_scream():
    script = os.path.join(os.getcwd(), "scream_to_type.py")
    if WINDOWS:
        subprocess.Popen(["start", "cmd", "/k", f"python {script}"], shell=True)
    else:
        subprocess.Popen(["python3", script])
    return render_template(
        "running.html",
        title="Scream-to-Type Running",
        emoji="🎤",
        message="Scream detection started..."
    )

@app.route("/useless_math")
def useless_math():
    results = []
    for _ in range(10):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        op = random.choice(["+", "-", "*", "/", "**"])
        try:
            result = eval(f"{a} {op} {b}")
        except Exception:
            result = "🤯 too useless to compute"
        results.append(f"{a} {op} {b} = {result}")
    return render_template("useless_math.html", results=results)

@app.route("/self_love")
def compliment():
    compliment_script = os.path.join(os.getcwd(), "compliment_ai.py")
    if WINDOWS:
        subprocess.Popen(["start", "cmd", "/k", f"python {compliment_script}"], shell=True)
    else:
        subprocess.Popen(["python3", compliment_script])

    return render_template(
        "running.html",
        title="Compliment AI Running",
        emoji="💗",
        message="Your compliment is on the way..."
    )

if __name__ == "__main__":
    app.run(debug=True)
