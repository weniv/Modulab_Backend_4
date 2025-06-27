
from environ import Env
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()

ENV_PATH = BASE_DIR / ".env"
env.read_env(ENV_PATH, overwrite=True)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m@g-y7f$et_l1tqy69fj6$q-l02iqj_ve&)y5#9gzr7*jw%v4)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

# 환경변수 문자열에서 콤마(,)를 구분자로 해서, 리스트로 자동 변환
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["127.0.0.1"],
)


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third apps
    'debug_toolbar',
    'django_bootstrap5',
    'django_extensions',
    # local apps
    'baemin',
    'blog',
    'chat',
]

MIDDLEWARE = [
    # TODO: DEBUG 상황에서만 적용되도록 할 거예요.
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 장고 앱 외적으로 별도의 템플릿을 쓸 경우,
        # 해당 템플릿 경로를 지정
        'DIRS': [
            BASE_DIR / "templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}       


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# 디폴트 언어 설정
LANGUAGE_CODE = 'ko-kr'  # 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# MEDIA_URL로 시작하는 URL 요청이 있다면
#  요청 파일을 MEDIA_ROOT 경로에서 찾아주겠다.
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 파이썬 기본에서 지원하는 환경변수 조회
# import os
# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# django-environ을 통해서 환경변수 조회 : 장고 친화적인 기능이 많아요.

# 환경변수에 OPENAI_API_KEY가 있으면 반환하고, 없으면 대신 None 반환
OPENAI_API_KEY = env.str('OPENAI_API_KEY', default=None)
# 환경변수에 UPSTAGE_API_KEY가 있으면 반환하고, 없으면 대신 None 반환
UPSTAGE_API_KEY = env.str('UPSTAGE_API_KEY', default=None)


# django-debug-toolbar를 보여줄 아이피
#  - 장고 서버를 구동한 컴퓨터에서 직접 접속했을 때에만 DDT를 보여주겠다.
#  - 다른 컴퓨터에서 접속했을 때에는 DDT가 보여지지 않아요.
INTERNAL_IPS = ["127.0.0.1"]

# DDT 추가 설정
#  - 기본 구성으로는 INTERNAL_IPS에 지정된 주소로 접속했을 때에 무조건 DDT 보여줍니다.
#  - 커스텀으로 파이썬 함수를 통해 보여줄 지 말지를 결정해줄 수 있어요.
#    ngrok 을 통한 요청인지 여부를 판단해서, 결정해줄 수 있을 듯 합니다.
