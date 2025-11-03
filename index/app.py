from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>AL SANA SİTE</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f2f2;
            text-align: center;
            margin-top: 100px;
        }
        input {
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 15px;
            font-size: 16px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 8px;
        }
        img {
            margin-top: 20px;
            width: 300px;
            border-radius: 10px;
            box-shadow: 0 0 10px #999;
        }
    </style>
</head>
<body>
    <h1>Adını gir</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Kullanıcı adını gir">
        <button type="submit">Göster</button>
    </form>

    {% if photo %}
        <div>
            <img src="{{ url_for('static', filename=photo) }}">
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    photo = None
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        if username == "hira":
            photo = "foto1.jpg"
        elif username == "beren":
            photo = "foto2.jpg"
        else:
            photo = "default.jpg"
    return render_template_string(HTML, photo=photo)

if __name__ == "__main__":
    app.run(debug=True)
