
from django.shortcuts import render
from datetime import datetime
import requests
from django.templatetags.static import static 
from django.utils.translation import gettext as _

NASA_API_URL = 'https://api.nasa.gov/planetary/apod'
NASA_API_KEY = 'xgbprF9SyPJs5cFNUXfbeQi8A7F2yVFZYIg2xcxw'

def home(request):
    try:
        nasa_data = get_nasa_apod()
        #print("NASA Data: ", nasa_data)  # Debugging print
    except Exception as e:
        print("Error: ", e)
        nasa_data = {}

    title = nasa_data.get("title", "No Title")
    img_url = nasa_data.get("url", "")  # Use a fallback if no URL

    # Check if the URL is a video
    if not img_url.endswith(('.jpg', '.jpeg', '.png', '.gif')): 
        # Use a static fallback image if it's a video
        img_url = static('images/fallback.jpg')  
        title = "Bode's Galaxy"

    date_object = datetime.strptime(nasa_data.get("date", "2024-01-01"), "%Y-%m-%d")
    formatted_date = date_object.strftime("%B %d, %Y")

    context = {
        "url": img_url,
        "date": formatted_date,
        "title": title,
    }

    #print("Context: ", context)  # Debugging print to check what we're passing to the template
    return render(request, "home.html", context)
    
# Get Astronomy Picture of the Day from NASA API
def get_nasa_apod():
    response = requests.get(NASA_API_URL, params={"api_key": NASA_API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error: Failed to retrieve Astronomy Picture of the Day")
