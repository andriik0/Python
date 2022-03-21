from django.urls import path
from .views import stub, news_item, list_news, create_news
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', stub, name='stub'),
    path('news/<int:post_id>/', news_item),
    path('news/create/', create_news),
    path('news/', list_news, name='list-news'),
]

urlpatterns += static(settings.STATIC_URL)