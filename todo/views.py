from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy


class TodoList(ListView):
    template_name = "list.html"
    model = TodoModel
    queryset = TodoModel.objects.filter(is_deleted=False)


class SuccessList(ListView):
    template_name = "success.html"
    model = TodoModel
    queryset = TodoModel.objects.filter(is_deleted=True)


class SuccessSave(UpdateView):
    template_name = "save.html"
    model = TodoModel
    fields = ("is_deleted",)
    success_url = reverse_lazy("success")


class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel
    queryset = TodoModel.objects.filter(is_deleted=False)


class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel
    fields = ("title", "memo", "priority", "duedate", "is_deleted")
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = TodoModel
    success_url = reverse_lazy("list")


class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = TodoModel
    fields = ("title", "memo", "priority", "duedate", "is_deleted")
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.is_deleted = True
        todo.save()
        return super().form_valid(form)
