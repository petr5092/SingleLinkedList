class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None




class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def push(self, num):
        node_part = Node(num)
        if not self.head:
            self.head = node_part
            self.tail = node_part
        else:
            self.tail.next_node = node_part
            self.tail = node_part

    def search_meaning(self, num):
        if self.head.value == num:
            return True
        x = self.head.next_node
        while x:
            if x.value == num:
                return True
            x = x.next_node
        return False

    def search_index(self, index):
        x = self.head
        if index == 0:
            return x.value
        for i in range(index):
            x = x.next_node
        return x.value

    def pop_meaning(self, num):
        x = self.head
        while x:
            if x.value == num:
                x.value = x.next_node.value
                x.next_node = x.next_node.next_node
                break
            if not x.next_node.next_node:
                x.next_node = None
                break
            x = x.next_node

    def pop_index(self, index):
        x = self.head
        if index == 0:
            x.value = x.next_node.value
            x.next_node = x.next_node.next_node
            return False
        for i in range(index - 1):
            x = x.next_node
        if x.next_node.next_node:
            x.next_node.value = x.next_node.next_node.value
            x.next_node.next_node = x.next_node.next_node.next_node
        else:
            print(x.value)
            x.next_node = None
            
    def exit(self):
        x = self.head
        answer = ''
        while x:
            answer += str(x.value) + ' -> ' 
            x = x.next_node
        return answer[:-4]



lst = SingleLinkedList()
for i in [0, 5, 10, 15, 20]:
    lst.push(i)
print(lst.exit())
print(lst.search_meaning(11))
print(lst.search_index(2))
lst.pop_index(4)
lst.pop_meaning(15)
print(lst.exit())
