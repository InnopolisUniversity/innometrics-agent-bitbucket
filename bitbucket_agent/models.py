from django.db import models


# class Actor(models.Model):
#     name = models.TextField()
#     emailAddress = models.EmailField()
#     displayName = models.TextField()
#     active = models.BooleanField()
#     slug = models.TextField()
#     type = models.TextField()


class Report(models.Model):
    eventKey = models.TextField()
    date = models.DateTimeField()
    actor = models.TextField()
    payload = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True, null=True)
