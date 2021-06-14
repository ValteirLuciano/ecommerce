from django.urls import path
from django.views.generic import TemplateView
from .views import home_page, about_page, contact_page


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]
