from django.urls import path, include

urlpatterns = [
    path('', include('student_management_app.urls'))
]