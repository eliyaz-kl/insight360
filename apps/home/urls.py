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
    path('allocate-vm', views.allocate_vm, name='allocate_vm'),
    path('ticket-created', views.ticket_created, name='ticket_created'),
    path('all-tickets-view', views.all_tickets_view, name='all_tickets_view'),
    path('ticket-open', views.ticket_open, name='ticket_open'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
