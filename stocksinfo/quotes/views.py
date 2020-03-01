from django.shortcuts import render, redirect
from .models import stocks
from .froms import StockForm
from django.contrib import messages
import json
import requests

def home (request):
	# pk_fb404108064241c48b15c2a796f46a9a
	

	# ticker = 'IBM'

	if request.method == "POST":

		ticker = request.POST['ticker']
		api_request =requests.get("https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_2fd1efae343441fca45deb7b490828c0")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = 'error'
		return render(request, 'home.html', {'api':api })

	else:
		return render(request, "home.html", {'ticker': "Enter a ticker symbol above..."})

	
	# return render(request, 'home.html', {'api':api })
	


	
def about (request):
	return render(request, 'about.html', {})

def add_stock(request):
	if request.method == "POST":
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, 'Stock has been added to the database!')
			return redirect('add_stock')

	else:
		ticker = stocks.objects.all()
		output = []
		for ticker_item in ticker:
			api_request =requests.get("https://sandbox.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=Tpk_2fd1efae343441fca45deb7b490828c0")

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = 'error'
		return render(request, 'add_stock.html', { 'ticker':ticker, 'output': output })

def delete(request, stock_id):
	item = stocks.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ('stock items have been deleted'))
	return redirect('add_stock')