import os
from pathlib import Path

import django
from correction_helper import code, fail, student_code, exclude_file_from_traceback
from django.test import Client

exclude_file_from_traceback(__file__)

os.environ["DJANGO_SETTINGS_MODULE"] = "proj.settings"
Path("proj/urls.py").write_text(
    """
from django.urls import path
from solution import hello

urlpatterns = [
    path('', hello),
]
"""
)
with student_code():
    django.setup()
    client = Client()
    content = client.get("/").content.decode()
if content != "Hello Django":
    fail("Expected `Hello Django`, got:", code(content))
