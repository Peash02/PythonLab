tasks = {}
def main():
    x = choices()
    choose(x)

def choices():
    print("1.Add Tasks.\n2.Remove a task.\n3.Update a Task.\n4.Sort Based on Priority.\n5.Print Task.\n6.Mark as Complete.")
    x = int(input("What do You Want to do?"))
    return x

def get_task():
    n = int(input("Enter the Number of Tasks:"))
    for i in range(n):
        ind = int(input("Enter the Task Index:"))
        desc = input("Enter the Task Description:")
        priority = input("Enter the Priority(High,Medium,Low):")
        add_task(ind,desc,priority)

def choose(x):
    match x :
        case 1:
            get_task()
            c = input("Do you want to make more changes?(y/n)")
            if c == 'y':
                main()
            else:
                exit()
        case 2:
            remove_task()
            c = input("Do you want to make more changes?(y/n)")
            if c == 'y':
                main()
            else:
                exit()
        case 3:
            update_desc()
            c = input("Do you want to make more changes?(y/n)")
            if c == 'y':
                main()
            else:
                exit()
        case 4:
            sort_task()
            c = input("Do you want to make more changes?(y/n)")
            if c == 'y':
                main()
            else:
                exit()
        case 5:
            print(tasks)
            c = input("Do you want to make more changes?(y/n)")
            if c == 'y':
                main()
            else:
                exit()
        case 6:
            mark_comp()
            c = input("Do you want to make more changes?(y/n)")
            if c == 'y':
                main()
            else:
                exit()
            

def add_task(task_no,description,priority):
    
    task = {
        'description':description,
        'priority' : priority.lower() ,
        'status' : 'Incomplete'
        }
    tasks[task_no] = task

def mark_comp():
    index = int(input("Enter the Index of Task to be marked As Complete:"))
    tasks[index]['status'] = 'Complete'
    print("Succesfully Marked as Complete.")

def remove_task():
    index = int(input("Enter the Index of task to be removed:"))
    tasks.pop(index)
    print("Successfully Removed Task.")

def update_desc():
    index = int(input("Enter the Task Index to be Updated:"))
    desc = input("Enter description to be updated:")
    tasks[index]['description'] = desc
    print("Updated Description Successfully.")

def sort_task():
    sorted_task = {}
    n = 1
    for i in range(1,len(tasks)+1):
        if tasks[i]['priority'] == 'high':
            sorted_task[n] = tasks[i]
            n +=1
    for i in range(1,len(tasks)+1):
        if tasks[i]['priority'] == 'medium':
            sorted_task[n] = tasks[i]
            n +=1
    for i in range(1,len(tasks)+1):
        if tasks[i]['priority'] == 'low':
            sorted_task[n] = tasks[i]
            n += 1
    print(sorted_task)
    
if __name__ == "__main__":
    main()
    
#END OF PROGRAM