from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
# Create your views here.

class Contact(APIView): 
    def post(self,request):
      content = request.data['content']
      sender = request.data['sender']
      send_mail(
			'Portfolio | Contact',
			content + "Envoyé par : " + sender,
			'guillaumedesurville99@gmail.com',
			['guillaumedesurville@gmail.com'],
			fail_silently=False)
      response = {
					'status': 'success',
					'code': status.HTTP_200_OK,
					'message': 'Message sent succesfully',
			}
      return Response(response)
    