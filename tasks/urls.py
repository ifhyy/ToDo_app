from django.urls import path
from .views import *

app_name = 'tasks'
urlpatterns = [
    path('', TasksListView.as_view(), name='task_list'),
    path('task/hisory/', TaskHistoryView.as_view(), name='task_history'),
    path('task/create/', TasksCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TasksDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TasksUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TasksDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/done', task_done, name='task_done'),
    path('task/history/delete', clear_history, name='task_history_clear')

]