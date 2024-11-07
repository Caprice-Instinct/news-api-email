import requests
from send_email import send_email

# Topic to get news of
topic = "tesla"

# Get API key from newsapi.org
api_key = "42e505d5f905406ab154e699a57346b4"

# url to get the news on a topic like Tesla; api key attached to it
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2024-10-07&sortBy=publishedAt"
       "&apiKey=42e505d5f905406ab154e699a57346b4&"
       "language=en")

# A request for content of url
request = requests.get(url)
# Convert the content into dictionary
content = request.json()

# Empty body for the email
body = "Subject: Today's news" + "\n"
# Iterate through the articles; access article titles and descriptions
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

# Update body into utf-8
body = body.encode("utf-8")

# Send email
send_email(message=body)
