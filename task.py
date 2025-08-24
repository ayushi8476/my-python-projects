tasks=[]
def to_do():
    print("--Your Tasks--")
    print("1.add the task")
    print("2.view the tasks")
    print("3.exit")
while True:
    to_do()
    choice=int(input("Enter your choice:"))
    if choice==1:
        task=(input("enter your task: "))
        tasks.append(task)
        print(f"task '{task}' added.")
    elif choice==2:
        if (len(tasks))==0:
            print("no tasks added")
        else:
            print("your tasks are:")
            for i,t in enumerate(tasks,1):
                print(f" {i} {t}")
    elif choice==3:
        print("good bye")
        break
    else: print("invaild choice")
    
        