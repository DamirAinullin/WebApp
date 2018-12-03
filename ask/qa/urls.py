from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('question/<int:id>/', question, name='question'),
    path('ask/', ask, name='ask'),
    path('popular/', popular, name='popular'),
    path('new/', popular, name='new')
]

