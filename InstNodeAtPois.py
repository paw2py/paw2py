#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    if not head or position < 0:
        return 
    if position == 0:
        head.data =  data
        return head
    
    curr = head # connect head and curr here 
    extra = SinglyLinkedListNode(data)
    #keep moving curr to next until we meet position 
    #on position connect extra node to next element of curr
    # reconnect extra node back to curr.next
    for i in range(0,position):
        if i+1 == position:             
            extra.next = curr.next
            curr.next = extra
            break            
        else:
            curr = curr.next
   
    return head  
    
