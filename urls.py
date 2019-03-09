print(' urls and paths')
from django.urls import path
import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path'', (empty string),
    path('aboutme', views.about_me),
    path('education', views.education),   
    path('funfacts', views.fun_facts),
    path('inclass', views.inclass),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

