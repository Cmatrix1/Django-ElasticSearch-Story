from django.urls import path
from shahvani.storys import views

app_name = "story"

urlpatterns = [
    path("<int:pk>", views.DetailStoryView.as_view(), name="detail"),
    path("", views.ListStoryView.as_view(), name="list"),
    path('search/', views.SearchView.as_view(), name='search'),
]
