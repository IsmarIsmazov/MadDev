CREATED_APP = [
    'apps.chairs',
    'apps.users',
    'apps.saving',
]

INSTALL_LIBRARY = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'jazzmin',
    'phonenumbers',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = CREATED_APP + INSTALL_LIBRARY + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]
