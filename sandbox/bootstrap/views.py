from django.shortcuts import render
from bootstrap.forms import ArticleForm


def example(request):
    form = ArticleForm()
    return render(request, "bootstrap/example.html", {"form": form})


def crispy(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
    else:
        form = ArticleForm()

    return render(request, "bootstrap/crispy.html", {"form": form})