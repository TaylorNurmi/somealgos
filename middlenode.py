class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node

        return self
class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

linkedList = LinkedList()	# create a new instance of a list
linkedList.add_to_front("1").add_to_front("2").add_to_front("3").add_to_front("4").add_to_front("5").add_to_front("6")

def middleNode(linkedList):
    runner = linkedList.head
    count = 0
    while (runner != None):
        runner = runner.next
        count += 1
    middle_node = count / 2
    if middle_node % 2 == 0:
        middle_node += 1
    runner = linkedList.head
    index = 1
    while runner != None:
        if index == middle_node:
            return runner.value, runner.next.value
        runner = runner.next
        index += 1
    return runner


print(middleNode(linkedList))
