
import streamlit_authenticator as stauth

def crear_login():
    credentials = {
        "usernames": {
            "admin": {
                "name": "Administrador",
                "password": ""  # Reemplaza con tu propio hash generado con bcrypt
            }
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        cookie_name="auth_cookie",
        key="auth_token",
        cookie_expiry_days=1
    )

    return authenticator




import streamlit_authenticator as stauth

def crear_login():
    credentials = {
        "usernames": {
            "admin": {
                "name": "Administrador",
                "password": "$2b$12$M5Uc9IHLTYUq5DCZMHm9fO9oyGXuV/QAlnVvu.76zbjbQ6NDXHVfa"  # Hash generado con bcrypt
            }
        }
    }

    authenticator = stauth.Authenticate(
        credentials=credentials,
        cookie_name="auth_cookie",
        key="auth_token",
        cookie_expiry_days=1
    )

    return authenticator
