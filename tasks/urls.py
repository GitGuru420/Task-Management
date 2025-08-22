from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, static_test, submit_task

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/',user_dashboard ),
    path('static/', static_test),
    path('submit-task/', submit_task),
]
