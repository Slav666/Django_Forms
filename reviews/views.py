from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
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

