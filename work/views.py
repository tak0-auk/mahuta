from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Work
from .form import WorkForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'work/index.html'
    context_object_name = 'work_list'

    # def get(self, request, *args, **kwargs):
    #     return Work.objects.all()
    def get_queryset(self):
        """ルートノードを返す　仕様は考え中"""
        return Work.objects.all()


class WorkCreateView(generic.CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'work/work_form.html'
    success_url = '/'


def work_index(request, name):
    node = get_object_or_404(Work, name=name)
    return render(request, 'work/work_index.html', {'node': node})
