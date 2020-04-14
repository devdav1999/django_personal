from django.urls import path

import views

urlpatterns = [
    path('about-me', views.homepage),
    path('contact-me', views.contact),
    path('my-projects', views.projects),
]

# Boilerplate to include static files.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static('static/', document_root=settings.STATIC_ROOT)

