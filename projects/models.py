from django.db import models
from django.contrib.postgres.fields import ArrayField

def project_image_directory_path(instance, filename):
    name = hash(instance.title)
    return f'photos/project/{name}'.format(filename=filename)  

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    code_url = models.CharField(max_length=500,blank=True,)
    project_url = models.CharField(max_length=500,blank=True)
    picture = models.ImageField(upload_to=project_image_directory_path, default='', max_length=1000, blank=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    language = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    def __str__(self):
        return self.title
