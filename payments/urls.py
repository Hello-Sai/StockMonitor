from django.urls import path

from payments.views import PaymentCreateView




urlpatterns = [
    path('payment/stocks',PaymentCreateView.as_view(),name="stock_payment")
]