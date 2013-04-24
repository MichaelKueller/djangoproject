from django.db import models

# Create your models here.
class Server(models.Model):    
    name = models.CharField(max_length=30)

class Artefact(models.Model):    
    artefactid = models.CharField(max_length=50)
    groupid = models.CharField(max_length=50)

class Deployment(models.Model):
    artefactid = models.ForeignKey(Artefact)
    version = models.CharField(max_length=30) 
    server = models.ForeignKey(Server)
    deploy_time = models.DateTimeField('time deployed')
    trigger = models.CharField(max_length=50) 
    outsidetimeframe = models.BooleanField(default = False)