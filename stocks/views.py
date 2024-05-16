from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView
from accounts.models import WatchList
from accounts.serializers import WatchListSerializer
from stocks.models import Stock
from stocks.serializers import StockSerializer

# Create your views here.

class GetStocksView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class WatchListModView(APIView):
    
    def get(self, request, *args, **kwargs):
        return Response(WatchListSerializer(request.user.watchlist.stocks.all(),many=True).data)


    def post(self, request, *args, **kwargs):
        print(request.data)
        print(request.data.get('action').lower() =='remove')
        if request.data.get('action').lower() =='remove':
            stock = request.user.watchlist.stocks.filter(id = request.data.get('stockId'))
            if stock.exists():
                print('remove executed')
                request.user.watchlist.stocks.remove(stock.first())
                return Response({'success':True,'message':'successfully removed'})
            return Response({'message' :'Stock has already removed' })
        elif request.data.get('action').lower() =='add' : 
            print('add executed')
            stock = Stock.objects.filter(id = request.data.get('stockId'))
            if stock.exists():
                request.user.watchlist.stocks.add(stock.first())
                return Response({'success':True,'message':'successfully added'})
            return Response({'message':'Stock has already added in watchlist'}) 
        return Response({'error':'Invalid Action'},status=400)
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)



