# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('ipa-form', views.ipa_form, name='ipa_form'),
    path('business-case', views.business_case, name='business_case'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
