from django.urls import path, re_path
from .views import index


urlpatterns = [
    # path('nedvizh/', index, name='nedvizh'),
    # path('electr/', index, name='electr'),
    re_path(r'^(?P<path>.+?)/$', index),
    # path('electr/plansh/', index, name='plansh'),
    # path('elecrt/telef/', index, name='telef'),
    # path('elecrt/telef/mobil/', index, name='mobil'),
    # path('nedvizh/arenda/', index, name='arenda'),
    # path('electr/telef/mobil/bolshie', index, name='bolshie')
]