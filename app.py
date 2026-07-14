from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Hiển thị trang portfolio."""

    skill_groups = [
        {
            "title": "Programming Languages",
            "items": ["Python", "JavaScript", "SQL"],
        },
        {
            "title": "Backend",
            "items": ["Flask", "Jinja2", "REST API"],
        },
        {
            "title": "Frontend",
            "items": ["HTML", "CSS", "Bootstrap"],
        },
        {
            "title": "Database",
            "items": ["SQLite", "MySQL"],
        },
        {
            "title": "Tools",
            "items": ["Git", "GitHub", "VS Code", "Postman"],
        },
    ]

    projects = [
        {
            "name": "Portfolio Website",
            "description": (
                "Website portfolio cá nhân được xây dựng bằng "
                "Python, Flask, Jinja2 và Bootstrap."
            ),
            "technologies": [
                "Python",
                "Flask",
                "Bootstrap",
            ],
            "github_url": "https://github.com/TuanHung20061006",
            "demo_url": "#",
        },
        {
            "name": "Task Management App",
            "description": (
                "Ứng dụng mẫu giúp người dùng quản lý và "
                "theo dõi các công việc cá nhân."
            ),
            "technologies": [
                "Python",
                "Flask",
                "SQLite",
            ],
            "github_url": "#",
            "demo_url": "#",
        },
        {
            "name": "Data Dashboard",
            "description": (
                "Dashboard mẫu dùng để trực quan hóa dữ liệu "
                "và hiển thị các chỉ số quan trọng."
            ),
            "technologies": [
                "Python",
                "JavaScript",
                "Bootstrap",
            ],
            "github_url": "#",
            "demo_url": "#",
        },
    ]

    return render_template(
        "index.html",
        name="Cao Tuấn Hùng",
        role="Nghiên cứu sinh tại Đại Học Công Nghiệp Hà Nội",
        current_year=datetime.now().year,
        skill_groups=skill_groups,
        projects=projects,
    )


if __name__ == "__main__":
    app.run(debug=True)