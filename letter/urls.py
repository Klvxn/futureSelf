from django.urls import path

from .views import HomeView, IndexView, LetterCreateView, LetterDetailView, LettersListView


app_name = 'letter'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('public_letters/', IndexView.as_view(), name='public_letters'),
    path('my-letters/', LettersListView.as_view(), name='my_letters'),
    path('letters/<uuid:pk>/', LetterDetailView.as_view(), name='letter_detail'),
    path('letters/create/', LetterCreateView.as_view(), name='create_letter'),
]
