'''
Module for over-riding local Django settings because we generally make changes
in settings.py and forget to remove the specifics like DB and server
credentials, API keys, etc.

Note: NEVER COMMIT THIS FILE unless you have a new setting to add to this file
that varies or may vary in a different environment.
'''

# Local Database settings
DATABASES['default']['ENGINE'] = 'django.db.backends.'
DATABASES['default']['NAME'] = ''
DATABASES['default']['USER'] = ''
DATABASES['default']['PASSWORD'] = ''
DATABASES['default']['HOST'] = ''
DATABASES['default']['PORT'] = ''
