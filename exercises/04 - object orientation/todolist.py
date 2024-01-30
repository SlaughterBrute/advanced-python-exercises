

class to_do_list_item():
    def __init__(self, task_description, due_date):
        self.description = task_description
        self.due_date = due_date
        self.is_completed = False
    
    def complete(self):
        self.is_completed = True

class to_do_list():
    def __init__(self, tasks: list):
        self.tasks = tasks
    
    def get_tasks(self):
        return self.tasks
    
    def incomplete_tasks(self):
        return filter(lambda t: t.is_completed, self.tasks)
    
    def complete_task(self, index):
        self.tasks[index].complete()
    
    def complete_all(self):
        for task in self.tasks:
            task.complete()

tdl = to_do_list([to_do_list_item("T1",1), to_do_list_item("T2",2)])
print(tdl.get_tasks())