from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import TwilioRestClient
from private.secrets import ACCOUNT_SID, AUTH_TOKEN

from .forms import MessageForm

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

            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

            number = request.POST['number']
            message = request.POST['message']
            result = client.messages.create(to=number, from_="+14243512633", body=message)

            response = {'result': 'success!!!!!!!!!'}
            return JsonResponse(response)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()

    return render(request, 'send.html', {'form': form})

@csrf_exempt
def sent(request):

    return render(request)


