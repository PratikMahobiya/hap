from django.db import models

# Create your models here.
class Contact_form_model(models.Model):
	Name		= models.CharField(max_length=100)
	Email		= models.EmailField()
	Contact		= models.CharField(max_length=100)
	Message 	= models.TextField(max_length=1000)
	created_on  = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = "enquiry"
