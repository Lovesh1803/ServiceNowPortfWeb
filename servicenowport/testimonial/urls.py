from django.urls import path
from .views import testimonials_page

app_name = 'testimonial'

urlpatterns = [
    path('', testimonials_page, name='all'),
]
