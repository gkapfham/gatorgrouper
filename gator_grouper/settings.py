"""
Django settings for gator_grouper project.
Generated by 'django-admin startproject' using Django 2.1.7.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_oauth_key():
    """
    Look for secret_key.py and return the SECRET_KEY entry in it if the file exists.
    Otherwise, generate a new secret key, save it in secret_key.py, and return the key.
    """
    try:
        oauthkey = os.environ["GATOR_GROUPER_OAUTH"]
    except KeyError:
        raise Exception("Couldn't find the oauth key")

    return oauthkey


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = find_oauth_key()
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "453514482871-qsirra9cq462b2vhdb14jokvfi917ik0.apps.googleusercontent.com"
)
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "Gatorgrouper-survey"
LOGOUT_REDIRECT_URL = "Gatorgrouper-home"


def find_or_create_secret_key():
    """
    Look for secret_key.py and return the SECRET_KEY entry in it if the file exists.
    Otherwise, generate a new secret key, save it in secret_key.py, and return the key.
    """
    try:
        key = os.environ["GATOR_GROUPER_KEY"]
    except KeyError:
        raise Exception("Couldn't find the secret key")

    return key


# Make this unique, and do not share it with anybody.
SECRET_KEY = find_or_create_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTHENTICATION_BACKENDS = (
    "social_core.backends.open_id.OpenIdAuth",
    "social_core.backends.google.GoogleOpenId",
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

ALLOWED_HOSTS = ["http://gatorgrouper-env.vimdyhzfyw.us-east-2.elasticbeanstalk.com/",
                 "127.0.0.1",
                 ]

# Application definition

INSTALLED_APPS = [
    "gatorgrouper.apps.GatorgrouperConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "gator_grouper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ]
        },
    }
]

WSGI_APPLICATION = "gator_grouper.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "gatorgrouper.Professor"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGIN_REDIRECT_URL = "Gatorgrouper-home"

LOGIN_URL = "login"
