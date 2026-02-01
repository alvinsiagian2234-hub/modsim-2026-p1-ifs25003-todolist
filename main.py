from repositories.TodoRepository import TodoRepository as Repo
from services.TodoService import TodoService as Service
from views.TodoView import TodoView as View


def run_app():
    repo_instance = Repo()
    service_instance = Service(repo_instance)
    view_instance = View(service_instance)

    view_instance.show_todos()


if __name__ == "__main__":
    run_app()