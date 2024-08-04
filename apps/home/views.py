# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def ipa_form(request):
    context = {'segment': 'ipa-form'}

    html_template = loader.get_template('home/ipa-form.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def business_case(request):
    context = {'segment': 'business-case'}

    html_template = loader.get_template('business_case.html')
    return HttpResponse(html_template.render(context, request))
    # return render(request,'business-case.html')

@login_required(login_url="/login/")
def ticket_created(request):
    context = {'segment': 'ticket-created'}

    html_template = loader.get_template('home/ticket-created.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def bot_creation(request):
    context = {'segment': 'bot-creation'}

    html_template = loader.get_template('home/bot-creation.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def allocate_vm(request):
    context = {'segment': 'allocate-vm'}

    html_template = loader.get_template('home/allocate-vm.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def all_tickets_view(request):
    context = {'segment': 'all-tickets-view'}

    html_template = loader.get_template('home/all-tickets-view.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def ticket_open(request):
    context = {'segment': 'ticket-open'}

    html_template = loader.get_template('home/ticket-open.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
