from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view),
    path('home/', home),
    path('delete_plan/<int:num>/', delete_plan),
    path('edit/<int:num>/', edit),
    path('logut/', logout_view),

]
