from django.urls import path
from .views import HomeView, CategoryDetailView, ArtworkDetailView

app_name = 'portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categoria/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('obra/<slug:slug>/', ArtworkDetailView.as_view(), name='artwork_detail'),
]