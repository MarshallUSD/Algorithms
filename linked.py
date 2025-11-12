"""
Linked list --- Bu ma'lumotlarning tugunlari (node) orqali zanjir shaklida saqlovchi data structure. Pythonda u odatda class yordamida yoziladi va ko'proq o'quv maqsadida ishlatiladi, chunki amalyotda list yoki deque ishlatiladi.
Linked list nima? 
Linear DS: elementlar ketma-ket joylashadi, lekin array/list'dan farqli ravishda ular xotirada yonma-yon emas.
Node: har bir tugun ikki qismdan iborat---bu data va next.
Head: linked list'ning boshlanish nuqtasi
"""
"""""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, data):
        new_node=Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last=self.next
        last.next = new_node

    def dis(self):
        current=self.head
        while current:
            print(current.data, end=" --> ")
            current=current.next
        print("None")


s=LinkedList()
s.append(10)
s.append(20)
s.append(30)
s.append(40)

s.dis()

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Foydalanish:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # 10 -> 20 -> 30 -> None

