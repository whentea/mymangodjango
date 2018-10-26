from django.confs.urls import url
from sample import views


urlpatterns = [url('^$', views.HomePageView.as_view())]