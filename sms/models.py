from django.db import models
from twilio.rest import TwilioRestClient
from private.secrets import ACCOUNT_SID, AUTH_TOKEN, SENT_FROM


class Message(models.Model):
    """
    class for sending and logging text messages
    """
    number = models.CharField(max_length=14)
    message = models.CharField(max_length=140, null=True)
    sent = models.DateTimeField(auto_now=True)  # Timestamp of when it was sent

    def __str__(self):
        output = "{m} + {n}"
        output = output.format(m=self.message[:20], n=self.number)
        return output

    # Move the logic from the view to here in the Model for greater encapsulation
    def save(self, *args, **kwargs):
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(to=self.number, from_=SENT_FROM, body=self.message)
        super(Message, self).save(*args, **kwargs)


