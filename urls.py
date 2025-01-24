from django.urls import path

from . import views
app_name = 'Enquete'

urlpatterns = [
    path('',views.index, name ='index'),
    path('<int:question_id>/resultados/', views.resultados, name='resultados'),
    path('<int:question_id>/votacao/', views.votacao, name='votacao'),
]