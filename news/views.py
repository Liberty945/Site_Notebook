from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    task = Tasks.objects.order_by('number')
    return render(request, 'news/news.html', {'task': task})


class TasksDetailView(DetailView):
    model = Tasks
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class TasksUpdateView(UpdateView):
    model = Tasks
    template_name = 'news/update.html'

    form_class = TasksForm


class TasksDeleteView(DeleteView):
    model = Tasks
    success_url = '/news/'
    template_name = 'news/delete.html'


def create(request):   #проверка данных добавления в БД
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Неверно введены данные '

    form = TasksForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
