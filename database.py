from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    salary = db.Column(db.String(100), nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    linkedin_url = db.Column(db.String(300))
    education = db.Column(db.Text)
    work_experience = db.Column(db.Text)
    resume_url = db.Column(db.String(300))


def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

        if Job.query.count() == 0:
            sample_jobs = [
                Job(title="Data Analyst", location="Bengaluru, India", salary="Rs. 12,00,000"),
                Job(title="Backend Engineer", location="Remote", salary="Rs. 15,00,000"),
                Job(title="Frontend Engineer", location="Delhi, India", salary="Rs. 10,00,000"),
                Job(title="Data Scientist", location="San Francisco, USA", salary="$120,000")
            ]
            db.session.add_all(sample_jobs)
            db.session.commit()


def load_jobs_from_db():
    return Job.query.all()


def load_job_from_db(id):
    return Job.query.get(id)


def add_application_to_db(job_id, data):
    application = Application(
        job_id=job_id,
        full_name=data["full_name"],
        email=data["email"],
        linkedin_url=data.get("linkedin_url"),
        education=data.get("education"),
        work_experience=data.get("work_experience"),
        resume_url=data.get("resume_url")
    )
    db.session.add(application)
    db.session.commit()
    return application