from django.urls import path

import views

urlpatterns = [
    path('', views.homepage),
    path('contact-me', views.contact),
    path('my-projects', views.projects),
    path('my-repos', views.github_api)
]

# Boilerplate to include static files.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static('static/', document_root=settings.STATIC_ROOT)

