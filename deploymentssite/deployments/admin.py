from django.contrib import admin
from deployments.models import Deployment, Server, Artefact

class DeploymentAdmin(admin.ModelAdmin):
    
    list_display = ('artefactid', 'version', 'server', 'deploy_time')
    list_filter = ['deploy_time']
    search_fields = ['artefactid']
    date_hierarchy = 'deploy_time'

admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(Server)
admin.site.register(Artefact)