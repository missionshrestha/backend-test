from django.urls import path
from credentials import views

urlpatterns = [
    path('<int:pk>',views.CredentialRetrieve.as_view()),
    path('create',views.CredentialCreate.as_view()),

]