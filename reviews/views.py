from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             review = Review(
#                 user_name=form.cleaned_data["user_name"], review_text=form.cleaned_data["review_text"], rating=form.cleaned_data["rating"])
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thankyou.html"

class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
