import datetime
AWS_ACCESS_KEY_ID = "AKIAVGLHUEKHRMJ4TH3M"
AWS_SECRET_ACCESS_KEY = "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"
AWS_USERNAME = "web-user"
AWS_GROUP_NAME = "web-group"

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'webecombucket.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'webecombucket.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'webecombucket'
S3DIRECT_REGION = 'ap-south-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
 'Expires': expires,
 'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

PROTECTED_DIR_NAME = 'protected'
PROTECTED_MEDIA_URL = '//%s.s3.amazonaws.com/%s/' %( AWS_STORAGE_BUCKET_NAME, PROTECTED_DIR_NAME)

AWS_DOWNLOAD_EXPIRE = 5000 #(0ptional, in milliseconds)



