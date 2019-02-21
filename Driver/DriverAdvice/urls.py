from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Driver.DriverAdvice import views

urlpatterns = [
    url(r'^advices/$', views.AdviceList.as_view()),
    url(r'^advices/(?P<pk>\d+)$', views.AdviceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
