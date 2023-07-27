var deleteMiddle = function(head) {
    let t = []
    let l

    while (head)
    {
        t.push(head.val)
        head = head.next
    }
    t.splice(t.length/2, 1)
    
    while (t.length)
        l = new ListNode(t.pop(), l)
    
    if (l)
        return l
    return null

};

