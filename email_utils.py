# email_utils.py
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import os

mail = Mail()

def create_app(app):
    """Initialize mail with Flask app"""
    mail.init_app(app)
    return mail

def generate_verification_token(email):
    """Generate a secure token for email verification"""
    serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
    return serializer.dumps(email, salt='email-verification-salt')

def confirm_verification_token(token, expiration=3600):
    """Verify token and return email if valid"""
    serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
    try:
        email = serializer.loads(token, salt='email-verification-salt', max_age=expiration)
        return email
    except:
        return False

def send_verification_email(user_email, token):
    """Send verification email to user"""
    verify_url = f"{os.getenv('FRONTEND_URL')}/verify-email/{token}"
    
    msg = Message(
        subject="Verify Your Email - HelpSetu",
        sender=os.getenv('MAIL_USERNAME'),
        recipients=[user_email]
    )
    
    # HTML email template (you can make this prettier later)
    msg.html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2 style="color: #2c3e50;">Welcome to Social Issue Reporter!</h2>
        <p>Thank you for registering. Please verify your email address by clicking the button below:</p>
        <a href="{verify_url}" style="background-color: #3498db; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 20px 0;">Verify Email</a>
        <p>This link will expire in 1 hour.</p>
        <p>If you didn't create this account, please ignore this email.</p>
        <hr>
        <p style="font-size: 12px; color: #7f8c8d;">Social Issue Reporter Team</p>
    </body>
    </html>
    """
    
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False