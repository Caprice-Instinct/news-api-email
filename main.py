import requests
from send_email import send_email

# Get API key from newsapi.org
api_key = "42e505d5f905406ab154e699a57346b4"

# url to get the news on a topic like Tesla; api key attached to it
url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2024-10-05&sortBy=publishedAt&apiKey"
       "=42e505d5f905406ab154e699a57346b4")

# A request for content of url
request = requests.get(url)
# Convert the content into dictionary
content = request.json()

# Empty body for the email
body = ""
# Iterate through the articles; access article titles and descriptions
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"

# Update body into utf-8
body = body.encode("utf-8")

# Send email
send_email(message=body)