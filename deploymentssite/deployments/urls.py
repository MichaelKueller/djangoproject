from django.conf.urls import patterns, url

from deployments import views

urlpatterns = patterns('',
      # ex: /deployments/
    url(r'^$', views.index, name='index'),
    # ex: /deployments/5/
    url(r'^(?P<deployment_id>\d+)/$', views.detail, name='detail'),         
)