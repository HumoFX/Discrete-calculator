from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ConditionForm


def index(request):
    return render(request, "index.html")


def encode(request):
    return render(request, "encode.html")


# def huffman(request):
#     return render(request, "huffman.html")


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

def to_list(cond: str) -> list:
    numbers = cond.split(' ')
    map_cond = map(int, numbers)
    numbers = list(map_cond)
    return numbers


def do_sum(cond: str):
    numbers = to_list(cond)
    result = sum(numbers)
    return result


class HuffmanView(generic.FormView):
    template_name = 'huffman.html'
    form_class = ConditionForm
    success_url = '/huffman/'
    plus_context = dict()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plus_context'] = self.plus_context
        return context

    def form_valid(self, form):
        condition = form.data.get('condition')
        if condition:
            self.plus_context['result'] = do_sum(condition)
        return super().form_valid(form)
