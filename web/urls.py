from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^submit/expense/$', views.submit_expense , name='submit_expense'),
    re_path('^submit/income/$', views.submit_income , name='submit_income'),
]