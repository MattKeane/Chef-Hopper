from django.db import models

class ScrapeException(models.Model):
	url = models.CharField(max_length=511)
	exception_type = models.CharField(max_length=31)
	occurence = models.DateField("when the error occurred")