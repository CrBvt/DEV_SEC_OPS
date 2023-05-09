import os
import sys
import subprocess

# static_test = subprocess.Popen('pytest django_node/static_tests')
static_test = subprocess.Popen('pytest static_tests')
static_test.communicate()
if static_test.returncode != 0:
    print("Static Tests FAILED")
    sys.exit(-1)

# os.system('django_node/manage.py runserver 0.0.0.0:8000')
django_app = subprocess.Popen('manage.py runserver 0.0.0.0:8000')

dynamic_test = subprocess.Popen('pytest dynamic_tests')
dynamic_test.communicate()
if dynamic_test.returncode != 0:
    print("Dynamic Tests FAILED")
    django_app.kill()
    sys.exit(-1)

django_app.communicate()