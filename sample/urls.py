from django.conf.urls import url
from sample import views


urlpatterns = [
    url('^$', views.HomePageView.as_view()),
    url('^about/$', views.AboutPageView.as_view()), #about page
    url('^help/$', views.HelpPageView.as_view()), #about help
]