from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from .models import To_do
from .forms import To_doForm

today = datetime.datetime.today().date()

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'to_do_list/index.html'

    def get_context_data(self, **kwargs):
        incomplete_task = To_do.objects.filter(states="2", deadline__gt=today).all().order_by('deadline')
        after_deadline_task = To_do.objects.filter(states="2", deadline__lte=today).all().order_by('deadline')

        context = super().get_context_data(**kwargs)
        context["today"] = today
        context["complete_task"] = To_do.objects.filter(states="1").all().order_by('deadline')
        context["incomplete_task"] = incomplete_task
        context["after_deadline_task"] = after_deadline_task
        context["form"] = To_doForm()

        # グラフのデータ取得
        number_of_incomplete_task = incomplete_task.count()
        number_of_after_deadline_task = after_deadline_task.count()
        context["number_of_incomplete_task"] = number_of_incomplete_task
        context["number_of_after_deadline_task"] = number_of_after_deadline_task

        number_of_task = []
        number_of_task.append(number_of_incomplete_task)
        number_of_task.append(number_of_after_deadline_task)
        context["number_of_task"] = number_of_task

        return context
    
    def post(self, request):
        to_do = To_do()
        to_do_form = To_doForm(request.POST, instance=to_do)
        to_do_form.save()

        return redirect(to='/')
    
    
# タスク状態変更時の処理
def Condition(self, num):

    task = To_do.objects.get(id=num)
    if task.states == "1":
        task.states = "2"
        task.save()
    else:
        task.states = "1"
        task.save()

    return redirect(to='/')

# 削除時の処理
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = To_do
    template_name = 'to_do_list/delete.html'
    success_url = reverse_lazy('index')


# 更新時の処理
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = To_do
    template_name = 'to_do_list/update.html'
    fields = ('deadline', 'task')
    success_url = reverse_lazy('index')

