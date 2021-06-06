from . import views
from django.urls import path

urlpatterns = [
    path('quiz/<int:pk>/result/', views.quiz_result_view, name='eng-quiz-result-view'),
    path('quiz/<int:pk>/save/', views.quiz_save_view, name='eng-quiz-save-view'),
    path('quiz/<int:pk>/data/', views.quiz_data_view, name='eng-quiz-data-view'),
    path('quiz/<int:pk>/', views.quiz_view, name='eng-quiz-view'),
    path('quiz/', views.quiz_list.as_view(), name='eng-quiz'),
    path('', views.main, name='eng-main'),

]