✅ Overview
Refactored a legacy Flask-based user management API into a clean, modular, secure, and maintainable application. Preserved all original functionality while improving architecture, code clarity, and production-readiness.

🔍 Major Issues Identified
Poor code organization: Monolithic structure with tight coupling

No data validation: Accepts any input, increasing risk

Plaintext passwords: Critical security flaw

Missing error handling: APIs crash or miscommunicate failure

No testing: No baseline for reliability

SQL injection potential: Unsafe DB operations

Unclear HTTP status codes: 200s used incorrectly

No modularity: Business logic and routes tightly entangled

✅ Changes Made
Modular Structure: Introduced /models, /routes, /schemas, /utils

ORM Integration: Used Flask-SQLAlchemy for safe and readable DB operations

Password Hashing: Integrated bcrypt for secure password storage

Input Validation: Used marshmallow-sqlalchemy schemas for input/output validation

HTTP Status Codes: Standardized all responses (201 for create, 404 for not found, etc.)

Error Handling: Used get_or_404() and custom validation

Database Initialization: Added init_db.py script

Test Readiness: Structure prepared for pytest-based unit testing

🔐 Security Improvements
Passwords are now hashed before DB insertion

No sensitive data returned in plain responses

Input payloads are validated and sanitized

⚙️ Tech Stack Used
Python 3.12

Flask

Flask-SQLAlchemy

Marshmallow

bcrypt

SQLite (local testing DB)

pytest (for unit test scaffolding)