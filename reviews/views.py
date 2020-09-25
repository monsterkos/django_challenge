from django.shortcuts import redirect, reverse
from books import models as book_models
from movies import models as movie_models
from . import forms
from . import models


def create_review(request, obj):
	if request.method == "POST":
		form = forms.CreateReviewForm(request.POST)
		if request.GET.get("kind") == "book":
			try:
				book = book_models.Book.objects.get(pk=obj)
				if form.is_valid():
					review = form.save()
					review.book = book
					review.created_by = request.user
					review.save()
					return redirect(reverse("books:book", kwargs={"pk":book.pk}))
			except book_models.Book.DoesNotExist:
				return redirect(reverse("core:home"))
		elif request.GET.get("kind") == "movie":
			try:
				movie = movie_models.Movie.objects.get(pk=obj)
				if form.is_valid():
					review = form.save()
					review.movie = movie
					review.created_by = request.user
					review.save()
					return redirect(reverse("movies:movie", kwargs={"pk":movie.pk}))
			except movie_models.Movie.DoesNotExist:
				return redirect(reverse("core:home"))
	return redirect(reverse("core:home"))

def delete_review(request, obj):
	if request.GET.get("kind") == "book":
		book = book_models.Book.objects.get(pk=obj)
		models.Review.objects.filter(created_by=request.user, book=book).delete()
		return redirect(reverse("books:book", kwargs={"pk":book.pk}))
	elif request.GET.get("kind") == "movie":
		movie = movie_models.Movie.objects.get(pk=obj)
		models.Review.objects.filter(created_by=request.user, movie=movie).delete()
		return redirect(reverse("movies:movie", kwargs={"pk":movie.pk}))
	return redirect(reverse("core:home"))