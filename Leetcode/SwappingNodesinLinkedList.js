var swapNodes = function(head, k) {
    let t = []
    let l

    while (head)
    {
        t.push(head.val)
        head = head.next
    }

    let temp = t[k-1]
    t[k-1] = t[t.length-k]
    t[t.length-k] = temp
    
    while (t.length)
        l = new ListNode(t.pop(), l)
    
    if (l)
        return l
    return null

};

