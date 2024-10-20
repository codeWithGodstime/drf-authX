# DRF AuthCore Boilerplate

## Overview

A customizable Django REST Framework (DRF) authentication boilerplate with JWT support, email verification, password reset, and a focus on **Test-Driven Development (TDD)**. This provides a flexible foundation without unnecessary routes or dependencies.

## Features

- Custom User Model
- JWT Authentication
- Email Verification
- Password Reset
- TDD-based Test Suite
- Minimal Dependencies

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/drf-auth-boilerplate.git
   cd drf-auth-boilerplate```

2. pip install -r requirements.txt
3. Set up .env:
   ```.env
   SECRET_KEY=your-secret-key
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   ```
4. python manage.py migrate
   ```
   python manage.py migrate
   ```

## Endpoints
- Register: /api/auth/register/
- Login: /api/auth/login/
- Logout: /api/auth/logout/
- Verify Email: /api/auth/verify-email/
- Password Reset: /api/auth/password-reset/
- Password Change: /api/auth/password-change/
