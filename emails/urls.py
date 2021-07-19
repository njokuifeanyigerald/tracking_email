from django.urls import path
from .views import *

urlpatterns = [
    path('send/render_image/', render_image, name='render_image'),
    path('send/',SendTemplateMailView.as_view(), name='send_template')
]
