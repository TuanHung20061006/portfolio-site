from datetime import datetime
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__, static_folder="public", static_url_path="")
BASE_DIR = Path(__file__).resolve().parent


def first_existing_public_file(*filenames):
    for filename in filenames:
        if (BASE_DIR / "public" / filename).is_file():
            return filename

    return None


@app.route("/")
def home():
    """Hiển thị trang portfolio."""

    skill_groups = [
        {
            "title": "Programming Languages",
            "skills": ["Python", "JavaScript", "SQL"],
        },
        {
            "title": "Backend",
            "skills": ["Flask", "Jinja2", "REST API"],
        },
        {
            "title": "Frontend",
            "skills": ["HTML", "CSS", "Bootstrap"],
        },
        {
            "title": "Database",
            "skills": ["SQLite", "MySQL"],
        },
        {
            "title": "Tools",
            "skills": ["Git", "GitHub", "VS Code", "Postman"],
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
            "image": "images/project/project-1.jpg",
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
            "image": "images/project/project-2.webp",
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
            "image": "images/project/project-3.jpg",
            "github_url": "#",
            "demo_url": "#",
        },
    ]

    avatar_image = first_existing_public_file(
        "images/avatar.jpg",
        "images/project/avatar_image.jpg",
    )

    return render_template(
        "index.html",
        name="Cao Tuấn Hùng",
        role="Nghiên cứu sinh tại Đại Học Công Nghiệp Hà Nội",
        current_year=datetime.now().year,
        skill_groups=skill_groups,
        projects=projects,
        avatar_image=avatar_image,
    )


if __name__ == "__main__":
    app.run(debug=True)
