from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Driver.DriverAdvice import views

urlpatterns = [
    url(r'^advices/$', views.AdviceList.as_view()),
    url(r'^advices/(?P<pk>\d+)$', views.AdviceDetail.as_view()),
    url(r'quizzes/$', views.QuizView.as_view()),
    url(r'^questions$', views.QuizQuestionView.as_view()),
    url(r'^answers/$', views.QuizAnswersView.as_view()),
    url(r'^forum/questions$', views.ForumQuestionsView.as_view()),
    url(r'^forum/answers/$', views.ForumAnswersView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
