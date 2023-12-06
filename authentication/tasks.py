from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes

__project_by__ = "RajeshKumar"

def send_password_reset(user_id):
    user = User.objects.get(pk=user_id)
    token_generator = PasswordResetTokenGenerator()
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

    subject = "Password Reset"
    token = token_generator.make_token(user)
    reset_link = f"http://127.0.0.1:8000/auth/password_reset_confirm/{uidb64}/{token}/"

    message = f"""
        <html>
        <body>
            <div style="position: relative; text-align: center; width: 1168px; height: 605px; margin: 0 auto; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5);"></div>
        <img src="https://s6.imgcdn.dev/ZjPxy.png" alt="ZjPxy.png" border="0" style="width: 100%; max-height: 500px;">
        <div
            style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-family: Arial, Helvetica, sans-serif; color: #fff; z-index: 1; background: rgba(0, 0, 0, 0.5); padding: 10px; line-height: 1.2; max-width: 80%;">
            <h1>Please click the below button</h1>
            <h3>To reset your password:</h3>
            <p style="text-align: center;">
                <a href="{reset_link}" target="_blank"
                    style="display: inline-block; padding: 10px 20px; background-color: #007BFF; color: #fff; text-decoration: none; border-radius: 5px;">RESET
                    PASSWORD</a>
            </p>
        </div>
        <footer
            style="position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); font-family: Arial, Helvetica, sans-serif; color: #fff; z-index: 1;">
            &copy; 2023 Online Grocery List. All rights reserved. | From Python Batch-2 Team
        </footer>
    </div>
        </body>
        </html>
    """
    email = EmailMessage(subject, message, "noreply@example.com", [user.email])

    email.content_subtype = "html"

    email.send()

    print("Password reset email successfully sent")
