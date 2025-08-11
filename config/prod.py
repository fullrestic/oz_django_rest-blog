from . local import *
# local에 있는 모든 항목을 불러와서 필요한 부분만 수정

DEBUG = False

ALLOWED_HOSTS = ['fullrestic.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}