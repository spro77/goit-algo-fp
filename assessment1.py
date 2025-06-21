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

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)
        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    a = list1.head
    b = list2.head
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

def main():
    list1 = LinkedList()
    list2 = LinkedList()

    for i in [1, 3, 5, 7]:
        list1.append(i)
    for i in [2, 4, 6, 8]:
        list2.append(i)

    print("List 1:", list1.to_list())
    print("List 2:", list2.to_list())

    merged_list = merge_sorted_lists(list1, list2)
    print("Merged List:", merged_list.to_list())

if __name__ == "__main__":
    main()