from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
import projects.views
import contact.views
import experiences.views


urlpatterns = [
    path('projects/',projects.views.ProjectsList.as_view()),
    path('experiences/',experiences.views.ExperiencesList.as_view()),
    path('contact/',contact.views.Contact.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

