from django.shortcuts import render
import razorpay
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
# Create your views here.
client = razorpay.Client(auth=(settings.RAZORPAY_KEY,settings.RAZORPAY_SECRET))

class PaymentCreateView(APIView):
    def post(self,request):
        context = {'key':client.auth[0]}
        print(request.data)
        data = {
            "amount": request.data.get('stock_amount')*100,
            "currency": "INR",
            "receipt": "receipt437298371",
            "notes": {
                "address": "park road",
                "key2": "value2"
            }
        }
        
        try:
            payment = client.order.create(data = data)
        except Exception as e:
            return Response({'error':str(e)},status=500)
        
        context.update(payment = payment,amount = payment.amount)
        return Response(context)