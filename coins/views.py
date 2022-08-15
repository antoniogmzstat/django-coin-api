from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coin
from .serializers import CoinSerializer
from django.shortcuts import render
import datetime


# Create your views here.
@api_view(['GET'])
def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def dashboard(request):
    return render(request, 'dashboard.html')


@api_view(['GET'])
def get_coin_list(request):

    coins = Coin.objects.values('Name', 'Symbol').distinct()
    list_coins = [{"name": coin["Name"], "symbol": coin["Symbol"]} for coin in coins]

    return Response(list_coins)

@api_view(['GET'])
def get_coin_close(request, name, start_date):
    # checking for the parameters from the URL
    # coins = Coin.objects.all()

    start_date_filter = datetime.datetime.strptime(start_date+' 23:59:59', '%Y%m%d %H:%M:%S').isoformat()
    coins = Coin.objects.filter(Name=name, Date=start_date_filter)
    
    serializer = CoinSerializer(coins, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_coin_profit(request, name, start_date, end_date):


    start_date_filter = datetime.datetime.strptime(start_date+' 23:59:59', '%Y%m%d %H:%M:%S').isoformat()
    end_date_filter = datetime.datetime.strptime(end_date+' 23:59:59', '%Y%m%d %H:%M:%S').isoformat()

    coin_interval = Coin.objects.filter(Name=name, Date__range=[start_date_filter, end_date_filter]).values()
    list_dict_coins = [coin for coin in coin_interval]
    
    dict_coin_max = max(list_dict_coins, key=lambda x:x['Close'])
    dict_coin_min = min(list_dict_coins, key=lambda x:x['Close'])    
    
    return Response({"max":dict_coin_max, "min": dict_coin_min, "data":list_dict_coins})
    