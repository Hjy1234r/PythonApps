if __name__ == '__main__':
    N = int(input(""))
    com_arr = []
    arr = []
    
    def chooseCOMMAND(userinput):
        com_arr = userinput.split()
        if len(com_arr) == 2:
            com_arr[1] = int(com_arr[1])
        elif len(com_arr) == 3:
            com_arr[2] = int(com_arr[2])
        match com_arr[0]:
            case "insert":
                arr.insert(com_arr[1], com_arr[2])
            case "print":
                print(arr)
            case "remove":
                arr.remove(com_arr[1])
            case "append":
                arr.append(com_arr[1])
            case "sort":
                arr.sort()
            case "pop":
                arr.pop()
            case "reverse":
                arr.reverse()
    for _ in range(0, N):
        command = input("")
        chooseCOMMAND(command)
        
        