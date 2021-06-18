from ll_zip.linked_list import Linkedlist
def zip_Lists(list1, list2):
    """
    this function , is takes two linked list
    and returned a new linked list-withc is merged of the two before
    """
    current1 = list1.head
    current2 = list2.head



    if not current1:
        list1.head = list2.head
        return list1.head
    if not current2:
        return list1.head


    pointer = current2.next

    while current1.next and current2.next:
        current2.next = current1.next
        current1.next= current2
        current1 = current2.next
        current2 = pointer
        pointer = pointer.next


    if not current1.next:
        current1.next = current2
        return list1.head

        
    if not current2.next:
        current2.next = current1.next
        current1.next = current2
        return list1.head








        
if __name__ == "__main__":
    ll1 = Linkedlist()
    ll2 = Linkedlist()
    ll1.append(10)
    ll1.append(34)
    ll2.append(42)
    ll2.append(54)
    ll2.append(57)
    ll2.append(64)
    print(ll1.__str__())
    print(ll2.__str__())
    zip_Lists(ll1,ll2)
    print(ll1.__str__())       