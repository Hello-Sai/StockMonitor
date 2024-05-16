from rest_framework import serializers

from stocks.models import Stock
class StockSerializer(serializers.ModelSerializer):
    is_watchlisted = serializers.SerializerMethodField()
    class Meta:
        model = Stock
        fields = "__all__"

    def get_is_watchlisted(self,obj):
        return self.context['request'].user.watchlist.stocks.filter(id = obj.id).exists() if hasattr(self.context['request'].user,'watchlist') else False