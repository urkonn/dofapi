from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from apiapp.models import Publicacion

class PublicacionResource(ModelResource):
    class Meta:
        queryset = Publicacion.objects.all()
        resource_name = 'publicacion'
        authorization = Authorization()
