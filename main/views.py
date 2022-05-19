from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ConditionForm


def index(request):
    return render(request, "index.html")


def encode(request):
    return render(request, "encode.html")


def huffman(request):
    return render(request, "huffman.html")


def hamming(request):
    return render(request, "hamming.html")


# def get_condition(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ConditionForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ConditionForm()
#
#     return render(request, "huffman.html", {'form': form})
