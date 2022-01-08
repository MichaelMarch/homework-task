#####
# Queue definition
##

queue = []

# add value at the end of the queue
def enqueue(value):
    queue.append(value)
    
# remove the topmost element of the queue
# and return its value    
def dequeue():
    if not empty():
        return queue.pop(0)
    else:
        return None
    
# return true if the queue is empty
def empty():
    return len(queue) == 0

# display queue
def display():
    for i in queue:
        print(i, end=" ")
    print()


