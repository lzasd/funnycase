class Lnode():
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_




class LinkedList():
    def __init__(self):
        self._head = Lnode(None)

    def is_empty(self):
        return self._head.next is None

    def prepend(self, elem):
        self._head.next = Lnode(elem, self._head.next)

    def append(self, elem):
        p = self._head
        while (p.next is not None):
            p = p.next
        p.next = Lnode(elem)

    def insert(self, elem, i):
        if i < 0 or not isinstance(i, int):
            raise ValueError('Invalid index')
        else:
            index = 0
            p = self._head
            while p is not None:
                if index == i:
                    p.next = Lnode(elem, p.next)
                    break
                else:
                    p = p.next
                    index += 1

    def pop(self):
        if self._head.next is None:
            raise ValueError('No element to pop')
        else:
            e = self._head.next.elem
            self._head.next = self._head.next.next
            return e

    def find(self, elem):
        p = self._head
        index = 0
        while p is not None:
            if p.next.elem == elem:
                return index
            else:
                p = p.next
                index += 1
        return 'Not find'

    def __str__(self):
        p = self._head
        temp = ''
        while p.next is not None:
            temp += str(p.next.elem)
            temp += '->'
            p = p.next
        temp += 'None'
        return temp

def print_link(link):
    list1 = []
    londe = link._head.next
    while londe:


        list1.append(londe.elem)
        londe = londe.next

    while list1:
        print(list1.pop())

if __name__ == '__main__':
    l1 = LinkedList()
    print(l1)

    l1.prepend(1)
    l1.prepend(2)
    print(l1)
    l1.append(3)
    l1.append(4)
    print(l1)
    l1.insert(5, 1)
    print(l1)
    l1.pop()
    print(l1)
    print(l1._head)

    print_link(l1)