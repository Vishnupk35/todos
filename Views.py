#authentication
#login
#view for listing all todos
#creatin new to do
#fetching specific to do.
#deleting specififc to do
from Todos_app.Models import users,todos
session={}
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user
def Log_in_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("You must login")
    return wrapper

class SignInView:
    def get(self,*args,**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("Login Success")
            print(session)
        else:
            print("invalid")

class TudosView:
    # view for listing all todos
    @Log_in_required
    def get(self,*args,**kwargs):
        return todos
class MyTodosView:
    @Log_in_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_todos=[todo for todo in todos if todo["id"]==userId]
        print(my_todos)

    @Log_in_required  # creatin new to do
    def post(self, *args, **kwargs):
        id = session["user"]["id"]
        kwargs["id"] = id
        todos.append(kwargs)

    @Log_in_required
    def delete(self,*args,**kwargs):
        id = session["user"]["id"]
        task_id=kwargs.get("task_id")
        tod=[todo for todo in todos if todo["id"]==id and todo["task_id"]==task_id]
        if tod:
            todo=tod[0]
            todos.remove(todo)
            print("Requested To do deleted successfully")
    @Log_in_required#delete requested post
    def delete(self,*args,**kwargs):
        id = session["user"]["id"]
        task_id=kwargs.get("task_id")
        data=[task for task in todos if task["task_id"]==task_id]
        if data:
            todo=data[0]
            todos.remove(todo)
            print("Requested To do task deleted successfully")
        else:
            print("Requested To do not found")
class TodoView:
    def get_object(self,id):
        verify=[todo for todo in todos if todo["task_id"]==id]
        return verify

    @Log_in_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        task_id=kwargs.get("task_id")
        instance=self.get_object(task_id)
        get_todo=[todo for todo in todos if todo["task_id"]==task_id]
        if instance:
            print(get_todo)
        else:
            print("Requested To do not available")






sign_in=SignInView()
sign_in.get(username="akhil",password="Password@123")
my=MyTodosView()
my.post(task_id=7,task="Reminder for school fees",status=False)
my.delete(task_id=7)
v=TodoView()
v.get(task_id=7)