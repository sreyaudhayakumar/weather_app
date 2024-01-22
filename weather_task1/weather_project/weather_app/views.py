from django.shortcuts import render
import json
import urllib.request

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e4adc2002201883c66101e1f0d50ccea').read()
        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon'])+ ' '  +
            str(json_data['coord']['lat']), 
            "temp" : str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }
    
    else:
        city = ''
        data = {}

    return render(request, 'home.html',{'city':city,'data':data})
