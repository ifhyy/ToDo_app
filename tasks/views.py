from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from .models import *
from django.urls import reverse_lazy
from django.http import HttpResponse


class TasksListView(View):
    template_name = 'tasks/task_list.html'

    def get(self, request):
        task_list = Task.objects.filter(active=True)
        ctx = {'task_list': task_list}
        return render(request, template_name=self.template_name, context=ctx)


class TaskHistoryView(View):
    template = 'tasks/task_history.html'

    def get(self, request):
        done_list = Task.objects.filter(active=False)
        ctx = {'done_list': done_list}
        return render(request, template_name=self.template, context=ctx)


class TasksDetailView(DetailView):
    model = Task



class TasksCreateView(CreateView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
    fields = ['title', 'description']


class TasksUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
    fields = ['title', 'description']


class TasksDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class TaskDone(View):

    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, id=pk)
        task.active = False
        task.save()
        return HttpResponse()


from django.http import HttpResponseRedirect


def task_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.active = False
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clear_history(request):
    instance = Task.objects.filter(active=False)
    instance.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
