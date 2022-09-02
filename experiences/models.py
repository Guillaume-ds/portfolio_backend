from email.policy import default
from django.db import models

def project_image_directory_path(instance, filename):
    name = hash(instance.title)
    return f'photos/experience/{name}'.format(filename=filename)  

defaultQuery = dict({
    "languages":[""],
    "tags":[""],
    "keywords":""    
    }
)

class Experience(models.Model):
    title = models.CharField(max_length=250,null=True)
    date_deb = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description1 = models.TextField()
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    lien = models.CharField(max_length=2500,blank=True,null=True,default="")
    queryParams = models.JSONField(null=True, blank=True,default=defaultQuery)
    
    def __str__(self):
        return self.title
        
    