"""
@copyright Wise One Realty 2018 All Rights Reserved
@author Michelle Mark

Settings for wiseonerealty.com project.
"""
import os
from django.core.urlresolvers import reverse_lazy

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
EMAIL_HOST = os.environ.get("EMAIL_HOST", "127.0.0.1")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 25)
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_LOCALTIME = True
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "web-developer@michellemark.me")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMINS = [('Michelle Mark', "web-developer@michellemark.me")]
ALLOWED_HOSTS = [".wiseonerealty.com"]
ROOT_URLCONF = 'wiseone.urls'
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/New_York'
SITE_ID = 2
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "media")
STATIC_ROOT = os.environ.get("STATIC_ROOT", "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'wiseone', 'static'),
)
FIXTURE_DIRS = [
    os.path.join(BASE_DIR, "fixtures"),
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'wiseone', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]
MIDDLEWARE = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_mfa.middleware.MfaMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)
INSTALLED_APPS = (
    'flat_responsive',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_mfa',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    'djangocms_text_ckeditor',
    'filer',
    'djangocms_link',
    'djangocms_picture',
    'easy_thumbnails',
    'djangocms_file',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'wiseone'
)
LANGUAGES = (
    ('en', gettext('en')),
)
CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}
PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}
CMS_TEMPLATES = (
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('homepage.html', "Home Page"),
    ('template_blog.html', 'Blog Template'),
    ('coming-soon.html', 'Coming Soon Page'),
)
CMS_PERMISSION = False
CMS_TOOLBAR_ANONYMOUS_ON = False
CMS_PLACEHOLDER_CONF = {
    'banner_image': {
        'plugins': ['Bootstrap4PicturePlugin',]
    },
    'home_jumbotron_top_left': {
        'plugins': ['TextPlugin',]
    },
    'home_jumbotron_top_right': {
        'plugins': ['TextPlugin',]
    },
    'home_jumbotron_bottom_left': {
        'plugins': ['TextPlugin',]
    },
    'home_jumbotron_bottom_right': {
        'plugins': ['TextPlugin',]
    },
    'home_jumbotron_centered': {
        'plugins': ['TextPlugin',]
    }
}
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USERNAME'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOSTNAME'),
        'PORT': os.environ.get('DB_PORT'),
        'CONN_MAX_AGE': 600,
    }
}
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)
CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('default', 'Default'),
    ('fullwidth', 'Full-Width'),
    ('display-desktop', 'Display Desktop/Tablet Only'),
    ('display-mobile', 'Display Mobile Only'),
    ('match_height', 'Match Height'),
    ('tile_overlay', 'Caption Overlay'),
    ('inline', 'Inline'),
)
CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE = 'boxed'
DJANGOCMS_PICTURE_TEMPLATES = [
    ('fullwidth', 'Full-Width'),
    ('match_height', 'Match Height'),
    ('tile_overlay', 'Caption Overlay'),
    ('inline', 'Inline'),
    ('display-desktop', 'Display Desktop/Tablet Only'),
    ('display-mobile', 'Display Mobile Only'),
    ('default', 'Default'),
]
DJANGOCMS_BOOTSTRAP4_TAG_CHOICES = ['div', 'section', 'article', 'header', 'footer', 'aside']
DJANGOCMS_BOOTSTRAP4_CAROUSEL_TEMPLATES = (
    ('default', 'Default'),
)
DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 12
DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = (
    ('container', 'Container'),
    ('container-fluid', 'Fluid container'),
)
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
    ('col', 'Column'),
    ('w-100', 'Break'),
    ('', 'Empty')
)
DJANGOCMS_BOOTSTRAP4_USE_ICONS = False
DJANGOCMS_BOOTSTRAP4_TAB_TEMPLATES = (
    ('default', 'Default'),
)
DJANGOCMS_BOOTSTRAP4_SPACER_SIZES = (
    ('0', '* 0'),
    ('1', '* .25'),
    ('2', '* .5'),
    ('3', '* 1'),
    ('4', '* 1.5'),
    ('5', '* 3'),
)
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
DJANGOCMS_VIDEO_TEMPLATES = [
    ('default', 'Default'),
    ('responsive', 'Responsive'),
]
