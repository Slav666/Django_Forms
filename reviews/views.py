from django.http import request
from django.http.response import HttpResponseRedirect
from django.views.generic.detail import DetailView
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView
from django.views import View
# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #   self.object and self.request from documentation
        loaded_review = self.object
        request = self.request
        # favourite_id = request.session["favourite_review"]
        favourite_id = request.session.get("favourite_review")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context


class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
