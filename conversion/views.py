import requests
from django.shortcuts import render
from django import forms
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import status

class CurrencyConversionForm(forms.Form):
    amount = forms.FloatField(label='Valor', required=False, 
                            widget= forms.TextInput(attrs={
                               'placeholder':'Digite o valor a ser convertido',
                               'required': 'True'
                            }))
    from_currency = forms.ChoiceField(choices=[('USD', 'USD'), ('BRL', 'BRL'), ('EUR', 'EUR'), ('BTC', 'BTC')], 
                                      label='Moeda de origem', widget= forms.Select(attrs={'required': 'True'}))
    to_currency = forms.ChoiceField(choices=[('USD', 'USD'), ('BRL', 'BRL'), ('EUR', 'EUR'), ('BTC', 'BTC')], 
                                    label='Moeda destino', required=False, 
                                    widget= forms.Select(attrs={'required': 'True'}))

def currency_converter(from_currency, to_currency, amount):
    api_key = 'b61ltE9OqnM1k87OcEvk27N31IikvoBu'
    endpoint = f'https://api.apilayer.com/exchangerates_data/latest?base={from_currency}&apikey={api_key}'

    response = requests.get(endpoint)
    data = response.json()

    conversion_rate = data['rates'][to_currency]
    converted_amount = amount * conversion_rate

    return converted_amount, conversion_rate

@require_http_methods(["GET"])
def convert_currency_api(request):
    try:
        amount = float(request.GET.get('amount'))
        from_currency = request.GET.get('from')
        to_currency = request.GET.get('to')

        converted_amount, conversion_rate = currency_converter(from_currency, to_currency, amount)

        response = {
            "status": "ok",
            "data": {
                "conversion_rate": conversion_rate,
                "converted_amount": converted_amount
            }
        }

        return JsonResponse(response, safe=False, status=status.HTTP_200_OK)
    
    except Exception as e:
        response_error = {
            "status": "nok",
            "data": {
                "error": str(e)
            }
        }
        return JsonResponse(response_error, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def convert_currency_view(request):
    form = CurrencyConversionForm()

    if request.method == 'POST':
        form = CurrencyConversionForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']

            converted_amount, conversion_rate = currency_converter(from_currency, to_currency, amount)

            context = {
                'amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'conversion_rate': conversion_rate,
                'converted_amount': converted_amount,
            }
            return render(request, 'conversion/convert_currency.html', context)
        
    context = {'form': form}
    return render(request, 'conversion/convert_currency.html', context)