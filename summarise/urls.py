from django.conf.urls import url
from summarise import views
urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^summarising',views.summarising,name = 'summarising'),
]
