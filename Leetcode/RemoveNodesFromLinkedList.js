var removeNodes = function(head) {
    let t=[]
    let l
    
    while (head != undefined)
    {
        while (t.length && t[t.length-1] < head.val)
            t.pop()
        t.push(head.val)
        head = head.next
    }
    
    if (t.length)
    {
        while (t.length)
            l = new ListNode(t.pop(), l)
        return l
    }
    return null
};

