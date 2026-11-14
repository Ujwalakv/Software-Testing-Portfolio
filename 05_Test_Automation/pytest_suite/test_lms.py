from conftest import login
from app import ai_service as ai


def test_courses_and_enrol(client):
    login(client)
    assert b"Python Fundamentals" in client.get("/courses").data
    client.post("/enroll/1")
    client.post("/enroll/1")  # enrolling twice must not duplicate
    assert client.get("/dashboard").data.count(b"Python Fundamentals") == 1


def test_student_cannot_add_material(client):
    login(client)
    assert client.post("/course/1/material", data={"title": "x", "content": "y"}).status_code == 403


def test_teacher_can_add_material(client):
    login(client, "teacher@lms.test", "Teacher@123")
    client.post("/course/1/material", data={"title": "New unit", "content": "Body"})
    assert b"New unit" in client.get("/course/1").data


def test_notes_require_topic(client):
    login(client)
    assert b"Enter a topic" in client.post("/learn", data={"topic": ""}).data


def test_notes_generated(client):
    login(client)
    r = client.post("/learn", data={"topic": "Recursion", "level": "Beginner", "style": "Simple explanation"})
    assert b"Recursion" in r.data


def test_quiz_scoring_and_dashboard(client):
    login(client)
    client.get("/quiz?topic=Recursion")
    with client.session_transaction() as s:
        answers = [q["answer"] for q in s["quiz"]["questions"]]
    form = {f"q{i}": a for i, a in enumerate(answers[:3])}  # 3 right, 2 skipped
    assert b"You scored 3 out of 5" in client.post("/quiz", data=form).data
    d = client.get("/dashboard").data
    assert b"Recursion" in d and b"3/5" in d


def test_quiz_fallback_shape():
    qs = ai.generate_quiz("Graphs", "", "Beginner")[0]
    assert len(qs) == 5 and all(len(q["options"]) == 4 and 0 <= q["answer"] < 4 for q in qs)


def test_markdown_is_escaped():
    assert "<script>" not in ai.to_html("## Hi\n- <script>alert(1)</script>")
def test_teacher_dashboard_and_restrictions(client):
    login(client, "teacher@lms.test", "Teacher@123")
    assert b"Recent student quiz results" in client.get("/dashboard").data
    assert client.post("/enroll/1").status_code == 403
    assert client.get("/quiz?topic=X").status_code == 403
    assert client.get("/learn").status_code == 403


def test_teacher_creates_course(client):
    login(client, "teacher@lms.test", "Teacher@123")
    r = client.post("/course/new", data={"title": "Algebra", "subject": "Maths", "description": "Basics"},
                    follow_redirects=True)
    assert b"Algebra" in r.data


def test_student_cannot_create_course(client):
    login(client)
    assert client.post("/course/new", data={"title": "x", "subject": "y", "description": "z"}).status_code == 403