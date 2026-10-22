from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if not prompt:
            return render_template("index.html", error="Please enter a prompt first.")
        return render_template("result.html", prompt=prompt)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
