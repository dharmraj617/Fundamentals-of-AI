def stack_operation(stack):
    while True:
        print("STACK OPERATION \n")
        print("1.push \n")
        print("2.pop \n")
        print("3.peek \n")
        print("4.display \n")
        print("5.Exit \n")

        choice = int(input("enter your choice : "))
        if choice == 1:
            item = int(input("enter the element : "))
            stack.append(item)
            print("pushed element is ", item)
        elif choice == 2:
            if len(stack) == 0:
                print("stack is empty")
            else:
                item = stack.pop()
                print("poped element is ", item)
        elif choice == 3:
            if len(stack) == 0:
                print("stack is empty")
            else:
                item = stack[-1]
                print("peak item is", item)
        elif choice == 4:
            if len(stack) == 0:
                print("stack is empty")
            else:
                print(stack)
        elif choice == 5:
            print("Exiting.....")
            break
        else:
            print("......invalid choice......")


stack = []

stack_operation(stack)