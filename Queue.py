def queue_operation(queue):
    while True:
        print("QUEUE OPERATION \n")
        print("1.enqueue \n")
        print("2.dequeue \n")
        print("3.peek \n")
        print("4.display \n")
        print("5.Exit \n")

        choice = int(input("enter your choice : "))

        if choice == 1:
            item = int(input("enter the item : "))
            queue.append(item)
            print("enqueued item is", item)
        elif choice == 2:
            if len(queue) == 0:
                print("queue is empty")
            else:
                item = queue.pop(0)
                print("dequeue item is", item)
        elif choice == 3:
            if len(queue) == 0:
                print("queue is empty")
            else:
                item = queue[0]
                print("Peek item is ", item)
        elif choice == 4:
            if len(queue) == 0:
                print("queue is empty")
            else:
                print("queue is", queue)
        elif choice == 5:
            print("Exiting.....")
            break
        else:
            print("......Invalid choice......")


queue = []
queue_operation(queue)