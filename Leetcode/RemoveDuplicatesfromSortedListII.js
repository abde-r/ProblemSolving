var deleteDuplicates = function(head) {
    let t=[], n=[]
    let l
    
    while (head != undefined)
    {
        let temp
        (head.next) ? temp = head.next.val : temp = -909
        
        if (head.val == temp)
            n.push(head.val)
        if (head.val != temp && !n.includes(head.val))
            t.push(head.val)
        head = head.next
    }
    
    if (t.length)
    {
        for (let i=t.length-1; i>=0; i--)
            l = new ListNode(t[i], l)
        return l
    }
    return null
};

