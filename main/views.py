from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def encode(request):
    return render(request, "encode.html")


def huffman(request):
    return render(request, "huffman.html")


def hamming(request):
    return render(request, "hamming.html")
