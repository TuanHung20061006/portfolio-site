from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Hiển thị trang chủ portfolio."""
    return render_template(
        "index.html",
        name="Tên của bạn",
        role="Python Backend Developer",
    )