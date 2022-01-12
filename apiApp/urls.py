from django.urls import path

from apiApp import apiviews


app_name = 'apiApp'
urlpatterns = [
    path('login/', apiviews.login, name='login'),
    path('register/', apiviews.register, name='register'),
    path('answer/create/', apiviews.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', apiviews.get_answer, name='get_answer'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='answer_update'),
    path('question/create/', apiviews.question_create, name='question_create'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='question_update'),
    path('choice/create/', apiviews.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='choice_update'),
    path('survey/create/', apiviews.survey_create, name='survey_create'),
    path('survey/update/<int:survey_id>/', apiviews.survey_update, name='survey_update'),
    path('survey/view/', apiviews.survey_view, name='survey_view'),
    path('survey/view/active/', apiviews.get_active_surveys, name='get_active_surveys')

]
