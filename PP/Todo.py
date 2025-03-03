tasks = {}
def add_task(task_no,description,priority):
    
    task = {
        'description':description,
        'priority' : priority.lower() ,
        'status' : 'Incomplete'
        }
    tasks[task_no] = task

def remove_task():
    index = int(input("Enter the Index of task to be removed:"))
    tasks.pop(index)

def update_desc():
    index = int(input("Enter the Task Index to be Updated:"))
    desc = input("Enter description to be updated:")
    tasks[index]['description'] = desc

def sort_task():
    sorted_task = {}
    n = 1
    for i in range(len(tasks)):
        if tasks[i]['priority'] == 'high':
            sorted_task[n] = tasks[i]
            n +=1
    for i in range(len(tasks)):
        if tasks[i]['priority'] == 'medium':
            sorted_task[n] = tasks[i]
            n +=1
    for i in range(len(tasks)):
        if tasks[i]['priority'] == 'low':
            sorted_task[n] = tasks[i]
            n += 1
    
    return sorted_task

if __name__ == "__main__":
    n = int(input("Enter the Number of Tasks:"))
    for i in range(n):
        ind = int(input("Enter the Task Index:"))
        desc = input("Enter the Task Description:")
        priority = input("Enter the Priority(High,Medium,Low):")
        add_task(ind,desc,priority)
    


