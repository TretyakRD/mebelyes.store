# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/w/workro7d/mebelyes.store/mebelyes')
sys.path.insert(1, '/home/w/workro7d/.local/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mebelyes.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()