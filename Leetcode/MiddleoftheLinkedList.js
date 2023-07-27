var middleNode = function(head) {
    let t = []
    let l

    while (head)
    {
        t.push(head.val)
        head = head.next
    }

    let c = t.length/2
    
    while (t.length > c)
        l = new ListNode(t.pop(), l)
    
    if (l)
        return l
    return null
};

