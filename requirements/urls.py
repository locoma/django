from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.Requirements.as_view(), name='requirements'),
    url(r'^/invitadas/$', views.RequirementsInvitadas.as_view(), name='requirementsinvitadas'),
    url(r'^/cupos/$', views.cupos, name='cupos'),
    url(r'^/exito/$', views.Exito.as_view(), name='exito'),

]
