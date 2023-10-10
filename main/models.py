from django.db import models


class ContactMe(models.Model):
    name = models.CharField(max_length=25)
    mobile_number = models.CharField(max_length=25)
    email_address = models.EmailField()
    email_subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.name}'
