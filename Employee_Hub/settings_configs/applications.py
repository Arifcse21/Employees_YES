
# Application definition

PRE_INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'rest_framework',
    'employee',
    'permissions',
    'roles'
]

INSTALLED_APPS = PRE_INSTALLED_APPS + PROJECT_APPS

