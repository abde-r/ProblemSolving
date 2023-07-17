var addTwoNumbers = function(l1, l2) {
    t1 = []
    t2 = []

    while (l1 != undefined)
    {
        t1.push(l1.val)
        l1 = l1.next
    }
    while (l2 != undefined)
    {
        t2.push(l2.val)
        l2 = l2.next
    }

    let rem=0
    let r = null

    while (t1.length || t2.length || rem) {
        let val1 = t1.pop() || 0;
        let val2 = t2.pop() || 0;

        let total = val1 + val2 + rem;
        rem = Math.floor(total / 10);

        let new_node = new ListNode(total % 10);
        new_node.next = r;
        r = new_node;
    }

    return r
};
