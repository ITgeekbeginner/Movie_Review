from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Movie, Review
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

class MovieReviewsView(View):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = Review.objects.filter(movie=movie)
        reviews_data = [{
            'user_id': review.user_id.username,
            'review': review.review,
            'created_at': review.created_at
        } for review in reviews]
        return JsonResponse(reviews_data, safe=False)


class ReviewCreateView(View):
    @csrf_exempt
    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        data = json.loads(request.body)
        user = User.objects.get(username=data['username'])
        review = Review.objects.create(
            user=user,
            movie=movie,
            review=data['review']
        )
        return JsonResponse({
            'id': review.id,
            'user': review.user.username,
            'review': review.review,
            'created_at': review.created_at
        })


class ReviewUpdateView(View):
    @csrf_exempt
    def put(self, request, review_id):
        data = json.loads(request.body)
        review = get_object_or_404(Review, id=review_id)
        review.review = data['review']
        review.save()
        return JsonResponse({
            'id': review.id,
            'review': review.review,
            'updated_at': review.updated_at
        })


class ReviewDeleteView(View):
    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return JsonResponse({'message': 'Review deleted successfully'}, status=204)
# Create your views here.
