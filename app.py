from flask import Flask, render_template, request, redirect, flash, url_for
from database import (
    db,
    init_db,
    get_jobs_query,
    load_job_from_db,
    add_application_to_db,
    load_applications_from_db,
    delete_application_from_db,
    load_application_from_db,
    update_application_in_db,
)
from forms import ApplicationForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///career_connect.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "career-connect-secret-key"

init_db(app)

@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    sort = request.args.get("sort", "").strip()
    page = request.args.get("page", 1, type=int)

    stmt = get_jobs_query(query, sort)
    pagination = db.paginate(stmt, page=page, per_page=4, error_out=False)

    return render_template(
        "home.html",
        jobs=pagination.items,
        pagination=pagination,
        query=query,
        sort=sort
    )

@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)

    if not job:
        return render_template("404.html"), 404

    return render_template("jobpage.html", job=job, errors={})

@app.route("/job/<int:id>/apply", methods=["POST"])
def apply_to_job(id):
    job = load_job_from_db(id)

    if not job:
        return render_template("404.html"), 404

    form = ApplicationForm(request.form)

    if not form.validate():
        return render_template("jobpage.html", job=job, errors=form.errors)

    application = add_application_to_db(job.id, request.form)
    flash("Application submitted successfully!", "success")

    return render_template(
        "application_submitted.html",
        application=application,
        job=job
    )

@app.route("/applications")
def list_applications():
    applications = load_applications_from_db()
    return render_template("applications.html", applications=applications)

@app.route("/applications/<int:id>/delete", methods=["POST"])
def delete_application(id):
    success = delete_application_from_db(id)

    if not success:
        flash("Application not found.", "danger")
        return redirect(url_for("list_applications"))

    flash("Application deleted successfully!", "danger")
    return redirect(url_for("list_applications"))

@app.route("/applications/<int:id>/edit")
def edit_application_page(id):
    application = load_application_from_db(id)

    if not application:
        return render_template("404.html"), 404

    return render_template("edit_application.html", application=application, errors={})

@app.route("/applications/<int:id>/update", methods=["POST"])
def update_application(id):
    application = load_application_from_db(id)

    if not application:
        return render_template("404.html"), 404

    form = ApplicationForm(request.form)

    if not form.validate():
        return render_template("edit_application.html", application=application, errors=form.errors)

    update_application_in_db(id, request.form)
    flash("Application updated successfully!", "info")
    return redirect(url_for("list_applications"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)