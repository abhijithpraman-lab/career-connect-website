from wtforms import Form, StringField, TextAreaField, validators

class ApplicationForm(Form):
    full_name = StringField("Full Name", [
        validators.Length(min=2, max=100, message="Full name must be between 2 and 100 characters.")
    ])

    email = StringField("Email", [
        validators.Length(min=6, max=120, message="Email must be between 6 and 120 characters."),
        validators.Email(message="Please enter a valid email address.")
    ])

    linkedin_url = StringField("LinkedIn URL", [
        validators.Optional(),
        validators.Length(max=300, message="LinkedIn URL is too long.")
    ])

    education = TextAreaField("Education", [
        validators.Optional(),
        validators.Length(max=500, message="Education must be under 500 characters.")
    ])

    work_experience = TextAreaField("Work Experience", [
        validators.Optional(),
        validators.Length(max=1000, message="Work experience must be under 1000 characters.")
    ])

    resume_url = StringField("Resume URL", [
        validators.Optional(),
        validators.Length(max=300, message="Resume URL is too long.")
    ])