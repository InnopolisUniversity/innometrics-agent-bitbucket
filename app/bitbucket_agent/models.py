from django.db import models


class Report(models.Model):
    eventKey = models.TextField()
    date = models.DateTimeField()
    actor = models.TextField()
    HMAC = models.TextField(null=True)
    payload = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True, null=True)
