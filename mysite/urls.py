from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blogsingle, name='blog-single'),
    path('contact/', views.contact, name='contact'),
    path('blanktemplate/', views.innerpage, name='blank-template'),
    path('portfolio/', views.portfoliodetail, name='portfolio-detail'),
]