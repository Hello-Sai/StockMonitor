from django.urls import path

from stocks.views import GetStocksView, WatchListModView

urlpatterns = [
    path('get_stocks_list',GetStocksView.as_view()),
    path('watchlist_modify',WatchListModView.as_view())
]