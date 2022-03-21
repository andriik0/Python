from datetime import datetime

from django.shortcuts import render, redirect
import json
from django.conf import settings
from .createnewsform import NewsForm
from django.core.exceptions import PermissionDenied


def stub(request):
    return redirect('news/')


def news_item(request, **kwargs):
    news_id = kwargs.get('post_id')
    news_list = get_newslist()

    if not news_list:
        return stub(request)

    newsitem = list(filter(lambda item: item['link'] == news_id, news_list))[0]

    return render(request, 'news/news_item.html', context={
        'post': newsitem,
    })


def create_news(request):
    if request.POST:
        news_list = get_newslist()

        if not news_list:
            news_list = []

        import random
        random.seed()
        link = int(random.uniform(100, 999))
        title = request.POST.get('title')
        text = request.POST.get('text')
        if not title or not text:
            raise PermissionDenied
        news_list.append({'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                          'title': title,
                          'text': text,
                          'link': link})

        save_newslist(news_list)
        return redirect('/news/')
    news_form = NewsForm(data={'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                               'title': '',
                               'text': '', })
    return render(request, template_name='news/createnews.html', context={'newsform': news_form})


def get_newslist():
    file_name = settings.NEWS_JSON_PATH
    with open(file_name, "r") as f:
        news_list = json.load(f)
    return news_list


def save_newslist(newslist):
    file_name = settings.NEWS_JSON_PATH
    with open(file_name, "w") as f:
        json.dump(newslist, f)


def list_news(request):
    news_list = get_newslist()

    if not news_list:
        return stub(request)

    search = request.GET.get('q')

    if search:
        news_list = list(filter(lambda x: search in x['title'] or search in x['text'], news_list))

    for item in news_list:
        item["date"] = datetime.strptime(item["created"], '%Y-%m-%d %H:%M:%S').date()

    date_list = sorted(list(set([x["date"] for x in news_list])), reverse=True)

    list_to_template = []

    for date in date_list:
        filtered_news = filter(lambda x: x['date'] == date, news_list)
        news_of_date = [{'link': x['link'], 'title': x['title'], } for x in filtered_news]
        news_of_date = sorted(news_of_date, key=lambda x: x['title'])
        list_to_template.append({'shortdate': date.strftime("%Y-%m-%d"), 'news': news_of_date})

    return render(request, 'news/news.html', context={'news_list': list_to_template})

def search_news(request):
    return list_news(request)