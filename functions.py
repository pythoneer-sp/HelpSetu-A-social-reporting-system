from flask_login import UserMixin
from datetime import datetime
def UserModel(db):   # called a factory function
    class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        fullname = db.Column(db.String(100), nullable=False)
        mobilenum = db.Column(db.String(20), unique=True, nullable=False)
        password_hash = db.Column(db.String(128), nullable=False)
        point = db.Column(db.Integer, default=0)
        profile_image = db.Column(db.String(120), nullable=True)

        is_verified = db.Column(db.Boolean, default=False)
        verification_token = db.Column(db.String(255), nullable=True)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)

        # Relationship with issues
        issues = db.relationship('IssueReport', backref='reporter', lazy=True)

    return User


"""
//  Code Explanation
--> def create_profile_db(db)
    # Here i'm importing `db` from app.py --> db = SQLAlchemy(app)
    The function paramter, `db` inherits everything from `db`

"""
def ReportModel(db):
    class Report(db.Model):
        __tablename__ = 'reports'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100))
        contact = db.Column(db.String(100))
        victim_name = db.Column(db.String(255))
        issue_type = db.Column(db.String(100))
        address = db.Column(db.String(255))
        state = db.Column(db.String(100))
        district = db.Column(db.String(100))
        block = db.Column(db.String(100))
        location = db.Column(db.String(100))
        child_photo = db.Column(db.String(255))
        more_details = db.Column(db.Text)

    return Report

def StateReportModel(db):
    class StateReport(db.Model):
        __tablename__ = 'state_reports'
        id = db.Column(db.Integer, primary_key=True)
        state_name = db.Column(db.String(100), unique=True, nullable=False)
        report_count = db.Column(db.Integer, default=0)

    return StateReport

def StakeholderModel(db):
    class Stakeholder(db.Model):
        __tablename__ = 'stakeholders'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
        organization_type = db.Column(db.String(20))  # 'NGO' or 'Government'
        issue_types = db.Column(db.JSON)  # ["Water", "Electricity", "Roads"]
        states = db.Column(db.JSON)  # ["Delhi", "Maharashtra"]
        is_verified = db.Column(db.Boolean, default=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)