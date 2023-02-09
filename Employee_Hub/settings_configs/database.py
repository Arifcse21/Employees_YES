import os

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE"),
        'HOST': os.environ.get("DB_HOST"),
        'USER': os.environ.get("DB_USER"),
        'NAME': os.environ.get("DB_NAME"),
        'PASSWORD': os.environ.get("DB_PASSWD"),
        'PORT': 5432,
        'OPTIONS': {'sslmode': 'require'},
        'TEST': {
            'NAME': os.environ.get("DB_NAME")
        }
    }
}
