from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('condition/<int:num>', views.Condition, name='condition'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
]
