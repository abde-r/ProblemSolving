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

    let s1 = t1.reverse()
    let s2 = t2.reverse()

    while (s1.length || s2.length || rem) {
        let val1 = s1.pop() || 0;
        let val2 = s2.pop() || 0;

        let total = val1 + val2 + rem;
        rem = Math.floor(total / 10);

        let new_node = new ListNode(total % 10);
        new_node.next = r;
        r = new_node;
    }

    var prev = null;
    var current = r;
    var next = null;
    while (current != undefined) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    r = prev;
    return r;
};

