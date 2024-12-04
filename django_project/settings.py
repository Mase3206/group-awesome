"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

import yaml

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
FORCE_SCRIPT_NAME = '/' + os.environ.get('SITE_NAME', '') if os.environ.get('SITE_NAME', '') != '' else ''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

try:
	with open('secrets.yml', 'r') as f1:
		secrets = yaml.safe_load(f1)
		print('Found secrets file.')
except FileNotFoundError:
	print('Secrets file not found in this directory. Setting the `secrets` dict to empty.')
	secrets = {}

# try to grab the key from the secrets.yml file
# if (key := secrets.get('django', {}).get('secret_key', None)):
# 	print('Using Django SECRET_KEY from secrets.')
# 	SECRET_KEY = key
# else:
# 	print('Secret key not found in secrets file. Using default (insecure!)')
# 	SECRET_KEY = 'django-insecure-4$6@5&r4%kex2%me935-8q^=ep=ufnyv89&i7@dx^68924o2q#'
# del key

# SECURITY WARNING: keep the secret key used in production secret! This will default to this insecure key if the SECRET_KEY variable isn't set in the environment.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-4$6@5&r4%kex2%me935-8q^=ep=ufnyv89&i7@dx^68924o2q#')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)


ALLOWED_HOSTS = [
	'localhost',
	'127.0.0.1',
	'csci258.cs.umt.edu',  # this is the url of the VM
]
INTERNAL_IPS = [
	'127.0.0.1',
	'localhost',
]


# Application definition

INSTALLED_APPS = [
	# --  Built-ins -- #
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	
	# -- 3rd-party apps -- #
	'debug_toolbar',
	'crispy_forms',
	'crispy_bootstrap5',
	'django_extensions',
	'allauth_ui',
	'widget_tweaks',
	'slippers',
	'star_ratings',

	# -- Allauth stuff --- #
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.github',
	'allauth.socialaccount.providers.openid_connect',
	
	# -- Local apps -- #
	# 'accounts',
	'profiles',
	'planetary',
	'stellar',
	'apod_app',

]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware', 
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	"allauth.account.middleware.AccountMiddleware",
]


ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / "templates" ],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'profiles.context_processors.user_profile',
			],
		},
	},

]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	# PostgreSQL database used in production
	'prod': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.environ.get('POSTGRES_DB'),
		'USER': os.environ.get('POSTGRES_USER'),
		'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
		'HOST': 'postgres',
		'PORT': '5432',
	},

	# SQLite3 database used for development and testing
	'local': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# defaults to local if not set in environment variable
default_database = os.environ.get('DJANGO_DATABASE', 'local')
# sets detected database to default
DATABASES['default'] = DATABASES[default_database]


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_USER_MODEL = 'accounts.SpaceTraveler'
AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]
AUTHENTICATION_BACKENDS = [
	# Needed to login by username in Django admin, regardless of `allauth`
	'django.contrib.auth.backends.ModelBackend',

	# `allauth` specific authentication methods, such as login by email
	'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
	'github': {
		'APPS': [
			{
				'client_id': 'Ov23lia2PJfGFjNGTPi4',
				'secret': '548f4217db504d8893d6661dffc9f3f1f9301aa9',
				# 'key': ...,
			} if os.environ.get('DJANGO_DATABASE', 'local') == 'local' else {
				'client_id': secrets['github']['client_id'],
				'secret': secrets['github']['secret'],
			}
		],
		'SCOPE': [
			'user',
			'email',
		]
	},
	# "openid_connect": {
	# 	# Optional PKCE defaults to False, but may be required by your provider
	# 	# Can be set globally, or per app (settings).
	# 	"OAUTH_PKCE_ENABLED": True,
	# 	"APPS": [
	# 		{
	# 			"provider_id": "my-server",
	# 			"name": "My Login Server",
	# 			"client_id": "your.service.id",
	# 			"secret": "your.service.secret",
	# 			"settings": {
	# 				"server_url": "https://my.server.example.com",
	# 				# Optional token endpoint authentication method.
	# 				# May be one of "client_secret_basic", "client_secret_post"
	# 				# If omitted, a method from the the server's
	# 				# token auth methods list is used
	# 				"token_auth_method": "client_secret_basic",
	# 				"oauth_pkce_enabled": True,
	# 			},
	# 		},
	# 		{
	# 			"provider_id": "other-server",
	# 			"name": "Other Login Server",
	# 			"client_id": "your.other.service.id",
	# 			"secret": "your.other.service.secret",
	# 			"settings": {
	# 				"server_url": "https://other.server.example.com",
	# 			},
	# 		},
	# 	],
	# },
}


LOGIN_URL = FORCE_SCRIPT_NAME + '/accounts/login'

ACCOUNT_SIGNUP_REDIRECT_URL = 'profiles:create'
SOCIALACCOUNT_SIGNUP_REDIRECT_URL = 'profiles:create'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ACCOUNT_EMAIL_REQUIRED = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N = True

TIME_ZONE = 'America/Denver'
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# URL path to serve static files from; ex: '/group-3/static/'
STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
# project static files location
STATICFILES_DIRS = [ BASE_DIR / "static" ]
# collected static files location; includes other apps, like admin
STATIC_ROOT = BASE_DIR / 'staticfiles'
# enable caching and compression when serving static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
ALLAUTH_UI_THEME = 'starry'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STAR_RATINGS_WIDGET_TEMPLATE = 'star_ratings/widget.html'


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            # "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
			"level": "INFO",
            "propagate": False,
        },
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

NASA_API_KEY = 'xgbprF9SyPJs5cFNUXfbeQi8A7F2yVFZYIg2xcxw'