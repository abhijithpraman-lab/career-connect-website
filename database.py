from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    salary = db.Column(db.String(120), nullable=False)

class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    linkedin_url = db.Column(db.String(300))
    education = db.Column(db.Text)
    work_experience = db.Column(db.Text)
    resume_url = db.Column(db.String(300))

def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

        if Job.query.count() == 0:
            jobs = [
                Job(title="Data Analyst", location="Bengaluru, India", salary="Rs. 12,00,000"),
                Job(title="Backend Engineer", location="Remote", salary="Rs. 15,00,000"),
                Job(title="Frontend Engineer", location="Delhi, India", salary="Rs. 10,00,000"),
                Job(title="Data Scientist", location="San Francisco, USA", salary="$120,000"),
                Job(title="ML Engineer", location="Hyderabad, India", salary="Rs. 18,00,000"),
                Job(title="DevOps Engineer", location="Pune, India", salary="Rs. 14,00,000"),
                Job(title="Product Analyst", location="Mumbai, India", salary="Rs. 13,00,000"),
                Job(title="Software Engineer", location="Chennai, India", salary="Rs. 11,00,000"),
            ]
            db.session.add_all(jobs)
            db.session.commit()

def get_jobs_query(query_text="", sort=""):
    stmt = db.select(Job)

    if query_text:
        search_pattern = f"%{query_text}%"
        stmt = stmt.where(
            or_(
                Job.title.ilike(search_pattern),
                Job.location.ilike(search_pattern)
            )
        )

    if sort == "title":
        stmt = stmt.order_by(Job.title.asc())
    elif sort == "location":
        stmt = stmt.order_by(Job.location.asc())
    else:
        stmt = stmt.order_by(Job.id.asc())

    return stmt

def load_job_from_db(id):
    return db.session.get(Job, id)

def add_application_to_db(job_id, data):
    application = Application(
        job_id=job_id,
        full_name=data["full_name"],
        email=data["email"],
        linkedin_url=data.get("linkedin_url"),
        education=data.get("education"),
        work_experience=data.get("work_experience"),
        resume_url=data.get("resume_url"),
    )

    db.session.add(application)
    db.session.commit()
    return application

def load_applications_from_db():
    stmt = db.select(Application).order_by(Application.id.desc())
    return db.session.scalars(stmt).all()

def load_application_from_db(id):
    return db.session.get(Application, id)

def delete_application_from_db(id):
    application = db.session.get(Application, id)

    if not application:
        return False

    db.session.delete(application)
    db.session.commit()
    return True

def update_application_in_db(id, data):
    application = db.session.get(Application, id)

    if not application:
        return None

    application.full_name = data["full_name"]
    application.email = data["email"]
    application.linkedin_url = data.get("linkedin_url")
    application.education = data.get("education")
    application.work_experience = data.get("work_experience")
    application.resume_url = data.get("resume_url")

    db.session.commit()
    return application