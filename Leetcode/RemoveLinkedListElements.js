var removeElements = function(head, val) {
    let t = []
    let l

    while (head)
    {
        if (head.val != val)
            t.push(head.val)
        head = head.next
    }

    while (t.length)
        l = new ListNode(t.pop(), l)
    
    if (l)
        return l
    return null
};

