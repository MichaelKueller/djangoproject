# Create your views here.
from django.http import HttpResponse
from deployments.models import Deployment

def index(request):    
    latest_deployments_list = Deployment.objects.order_by('-deploy_time')[:5]
    output = ', '.join([p.version for p in latest_deployments_list])
    return HttpResponse(output)    

def detail(request, deployment_id):
    return HttpResponse("You're looking at deployment %s." % deployment_id)

