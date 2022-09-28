from django.db import models

# Create your models here.
class Contact(models.Model):
	name		= models.CharField(max_length=100)
	email		= models.EmailField()
	contact		= models.CharField(max_length=100)
	message 	= models.TextField()
	created_on  = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = "enquiry"
