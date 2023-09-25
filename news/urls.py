from django.urls import path
from . import views

urlpatterns = [                   #перенаправление на views
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TasksDetailView.as_view(), name='tasks-detail'),
    path('<int:pk>/update', views.TasksUpdateView.as_view(), name='tasks-update'),
    path('<int:pk>/delete', views.TasksDeleteView.as_view(), name='tasks-delete')
]