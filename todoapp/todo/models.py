from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
	item_name = models.CharField(max_length=255)
	item_status = models.CharField(max_length=20)
	created_date = models.DateTimeField('date created')

	def __str__(self):
		return self.item_name