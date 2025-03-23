from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('shop',views.shop,name='shop'),
    path('why',views.why,name='why'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('contact',views.contact,name='contact')
]
