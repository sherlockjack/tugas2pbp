from django.urls import path,include
from todolist.views import createtask, show_todolist #Jika masih abu abu buatlah modul bernama show todolist!   
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import deletetask
from todolist.views import finishedtask
from todolist.views import add_task
from todolist.views import show_todolist_json
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('createtask/', createtask, name='createtask'),
    path("finishedtask/<int:id>", finishedtask, name="finishedtask"),
    path("deletetask/<int:id>", deletetask, name="deletetask"),
    path("json/", show_todolist_json, name="show_todolist_json"),
    path("add_task/", add_task, name="add_task"),
]