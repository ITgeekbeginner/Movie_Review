from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', views.MovieReviewsView.as_view(), name='movie_reviews'),
    path('movies/<int:movie_id>/reviews/create/', views.ReviewCreateView.as_view(), name='create_review'),
    path('reviews/<int:review_id>/update/', views.ReviewUpdateView.as_view(), name='update_review'),
    path('reviews/<int:review_id>/delete/', views.ReviewDeleteView.as_view(), name='delete_review'),
]
