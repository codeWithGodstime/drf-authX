import pytest
from django.urls import reverse
from django.core import mail

pytestmark = pytest.mark.django_db

def get_tokens(text):
    import re
    # Regex pattern to match uid and token
    pattern = r'http:\/\/localhost:3000\.com\/(.*?)\/(.*?)$'

    match = re.search(pattern, text, re.MULTILINE)

    if match:
        uid = match.group(1)
        token = match.group(2)
    else:
        return None

    return uid, token

class TestUserReset:

    def test_user_can_reset_password(self, client, user):
        url = reverse("users-reset-password")
        data = {
            'email': user.email
        }
        
        # Send the POST request to trigger the password reset
        response = client.post(url, data, format="json")
        
        # Check the response status and message
        assert response.status_code == 200
        assert response.data["message"] == "Password reset link has been sent to your mail"
        # Check that an email was sent
        assert len(mail.outbox) == 1
        
        # Check the subject of the email
        assert mail.outbox[0].subject == "Reset password link"
        
        # Optionally check the recipient and body of the email
        assert mail.outbox[0].to == [user.email]


    def test_reset_password_confirmation(self, client, user):

        url = reverse("users-reset-password")
        data = {
            'email': user.email
        }
        response = client.post(url, data, format="json")
        uid, token = get_tokens(mail.outbox[0].body)
        
        url = reverse("users-reset-password-confirmation")
        data = {
            "uid": uid,
            "token": token,
            "new_password": "timetokill0099_"
        }
        response = client.post(url, data)

        user.refresh_from_db()
        assert user.check_password("timetokill0099_")
        assert not user.check_password("timetokill01_") # old passowr has changed

    def test_change_password(self, client, user):
        # Log in the user
        client.force_authenticate(user=user)

        url = reverse("users-change-password")
        data = {
            "current_password": "timetokill01_",  # Current password
            "new_password": "new_password_123!"    # New password
        }
        
        response = client.post(url, data, format="json")
        
        assert response.status_code == 200  # Check for successful password change
        user.refresh_from_db()

        assert user.check_password("new_password_123!")  # Verify that the new password is set correctly

        assert not user.check_password("timetokill01_")  # Ensure old password is not valid
