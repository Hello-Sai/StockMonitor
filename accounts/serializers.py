from rest_framework import serializers
from accounts.models import WatchList
from stocks.serializers import StockSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
class WatchListSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(many=True)
    class Meta:
        model = WatchList
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username','password')

    def validate(self, data):
        data['password'] = make_password(data['password'])

        return data

