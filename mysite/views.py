from django.shortcuts import render, redirect
from django.contrib import messages
from . import models, forms

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html', {})

def blogsingle(request):
    return render(request, 'blog-single.html', {})

def innerpage(request):
    return render(request, 'inner-page.html', {})

def portfoliodetail(request):
    return render(request, 'portfolio-details.html', {})

def contact(request):
	if request.method == 'POST':
		c_form 		= forms.Contact_Form(request.POST)
		if c_form.is_valid():
			Name 		= request.POST.get('Name','')
			Email 		= request.POST.get('Email','')
			Contact		= request.POST.get('Contact','')
			Message 	= request.POST.get('Message','')
			form_obj 	= models.Contact_form_model(Name = Name, Email = Email, Contact = Contact,Message = Message)
			form_obj.save()
			messages.add_message(request, messages.INFO, "Thank You.. {}".format(Name))
			return redirect('/')
		else:
			messages.add_message(request, messages.INFO, 'Thank You for Giving your Precious Time.')
			return redirect('/')