from django.db import models
from tastypie.utils.timezone import now

class Publicacion(models.Model):
    description = models.TextField()
    link = models.URLField(max_length=200)

    def __unicode__(self):
        return u"%s" % (self.description)
    
