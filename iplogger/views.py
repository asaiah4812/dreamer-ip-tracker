from django.shortcuts import render
import requests

def iptracker(request):
    if request.method == 'POST':
        ip_address = request.POST['ip_address']
        results = get_ip_details(ip_address)
        return render(request, 'iplogger/index.html', {'results': results})
    else:
        return render(request, 'iplogger/index.html')

def get_ip_details(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "fail":
        return "Failed to track IP address"

    country = data["country"]
    city = data["city"]
    zip_code = data["zip"]
    latitude = data["lat"]
    longitude = data["lon"]
    network = data['isp']
    timezone = data['timezone']
    region = data['region']

    result = f"IP Address: {ip_address}\n"
    result += f"Country: {country}\n"
    result += f"City: {city}\n"
    result += f"Zip Code: {zip_code}\n"
    result += f"Latitude: {latitude}\n"
    result += f"Longitude: {longitude}\n"
    result += f"network: {network}\n"
    result += f"timezone: {timezone}\n"
    result += f"region: {region}\n"

    return result