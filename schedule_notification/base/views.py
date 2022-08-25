from django.shortcuts import render
from django.http import JsonResponse

import pusher

pusher_client = pusher.Pusher(
  app_id='your id',
  key='your key',
  secret='your secret key',
  cluster='ap2',
  ssl=True
)


# Create your views here.
def index(request):
    return render(request,"base/index.html")

def sendNotification(request):
    pusher_client.trigger('my-channel', 'my-event', {'message': 'Notification from django backend'})
    return JsonResponse({"data":"Success"})