import requests

def get_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'country': 'in',
        'apikey' : '08094c561d6e4c2199da445eaf5ba2e3'
    }

    response = requests.get(url,params)
    if response.status_code == 200:
        news_data = response.json()
        if news_data['status'] == 'ok' and news_data['totalResults'] > 0:
            print(news_data['articles'][1]['title'])
            return news_data['articles'][1]['title']

        else:
            print("No articles found.")       

    else:
        print('Failed to get latest news headlines ',response.status_code)

