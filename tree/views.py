from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from .models import Node

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'tree/index.html'
    context_object_name = 'root_list'

    def get_queryset(self):
        """ルートノードを返す　仕様は考え中"""
        return Node.objects.all().filter(is_root=True)


class DetailView(generic.DetailView):
    model = Node
    template_name = 'tree/detail.html'


def index(request):
    root_list = Node.objects.all()
    context = {
        'root_list': root_list,
    }
    return render(request, 'tree/index.html', context)


def detail(request, node_id):
    node = get_object_or_404(Node, pk=node_id)

    return render(request, 'tree/detail.html', {'node': node})


def save(request):
    pass
