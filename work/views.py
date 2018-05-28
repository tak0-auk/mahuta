from django.shortcuts import render, get_object_or_404
from django.template.base import kwarg_re
from django.views import generic
from django.urls import reverse_lazy

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


class WorkIndexView(generic.DetailView):
    model = Work
    template_name = 'work/work_index.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Work, name=self.kwargs['name'])


class WorkCreateView(generic.CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'work/work_form.html'
    success_url = '/'


class WorkUpdateView(generic.UpdateView):
    # model = Work
    form_class = WorkForm
    template_name = 'work/work_form.html'
    # success_url = reverse_lazy('work:work', kwargs={'name'})

    def get_object(self, queryset=None):
        return get_object_or_404(Work, name=self.kwargs['name'])

    # def get_success_url(self):
    #     reverse_lazy('work:work', kwargs={'name': self.kwargs.get('name', 'nai')})


def work_edit(request, name):
    work = get_object_or_404(Work, name=name)
    return render(request, 'work/work_edit.html', {'work': work})


def work_index(request, name):
    node = get_object_or_404(Work, name=name)
    return render(request, 'work/work_index.html', {'node': node})


def work_save(request, name):
    work = get_object_or_404(Work, name=name)
    work.name = request.POST['name']
    work.summary = request.POST['summary']
    work.save()
    return render(request, 'work/work_index.html', {'work': work})
