from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from .forms import MessageForm
from twilio import TwilioRestException
import datetime
# Create your views here.

@csrf_exempt
def send(request):
    """
    Default landing page for the entire application
    :return:
    """

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            try:
                number = request.POST['number']
                message = request.POST['message']
                this_message = Message(number=number, message=message)
                this_message.save()
                context = {'form': form, 'messages': "Sentit"}
            except TwilioRestException as e:
                context = {'form': form, 'messages': str(e)}


    # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()
        context = {'form': form}

    return render(request, 'send.html', context)



