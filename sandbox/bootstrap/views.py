from django.shortcuts import render
from bootstrap.forms import ArticleForm


def example(request):
    form = ArticleForm()
    return render(request, "bootstrap/example.html", {"form": form})