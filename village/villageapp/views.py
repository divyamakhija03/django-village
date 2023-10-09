from django.shortcuts import render,redirect
from django.http import HttpResponse
from grievanceapp.models import grievanceForm

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.
def home(request):
    return render(request,'villageapp/home.html')

def womenwelfare(request):
    return render(request,'villageapp/womenwelfare.html')

def appointmentcontact(request):
    return render(request,'villageapp/appointmentcontact.html')

def grievance(request):
    return render(request,'villageapp/grievance.html')

def savegrievance(request):
    if request.method=="POST":
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        aadhar_card = request.POST['aadhar']
        address = request.POST['address']
        issue = request.POST['issue']
        city = request.POST['city']
        pincode = request.POST['pincode']
        details=grievanceForm(first_name=first_name,last_name=last_name,email=email,aadhar_card=aadhar_card,address=address,issue=issue,city=city,pincode=pincode)
        details.save()
    return render(request,'villageapp/home.html')


def utility(request):
    currency = 'INR'
    amount = 70000  
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://localhost:8000/test/paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'villageapp/utility.html', context=context)

@csrf_exempt
def paymenthandler(request):
    return render(request, 'villageapp/home.html')
                