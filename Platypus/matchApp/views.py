from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context."}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('matchApp/login.html', context_dict, context)

def home(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('matchApp/home.html', context_dict, context)

def classpage(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('matchApp/classpage.html', context_dict, context)