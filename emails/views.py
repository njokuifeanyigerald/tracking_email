from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render
from .models import UserModel
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from PIL import Image

class SendTemplateMailView(APIView):
    def post(self, request, *args, **kwargs):
        target_user_email  = request.data.get('email')
        mail_template = get_template('emails/home.html')
        context_data_is  = dict()
        context_data_is['image_url'] = request.build_absolute_uri(('render_image'))
        url_is = context_data_is['image_url']
        context_data_is['url_is'] = url_is
        html_detail = mail_template.render(context_data_is)
        subject, from_email, to = 'greetings!!', 'postmaster@manojadhikary.com.np', [target_user_email]
        msg = EmailMultiAlternatives(subject, html_detail, from_email, to)
        msg.content_subtype = 'html'
        msg.send()
        return Response({'success': True})

@api_view()
def render_image(request):
    if request.method == 'PUT':
        image  = Image.new('RGB', (20,20))
        response = HttpResponse(content_type = 'image/png', status=status.HTTP_200_OK)
        user = UserModel.objects.get(id=1)
        user.status = True
        user.save()
        image.save(response, 'PNG')
        return Response

