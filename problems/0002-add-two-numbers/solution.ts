/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let carry = 0;
    let dummy = new ListNode();
    let curr = dummy;

    while (carry !== 0 || l1 !== null || l2 !== null) {
        let digit = new ListNode();
        curr.next = digit;

        const sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;
        digit.val = sum % 10;
        carry = Math.floor(sum / 10);

        if (l1 !== null) {l1 = l1.next;}
        if (l2 !== null) {l2 = l2.next;}
        curr = curr.next;
    }

    return dummy.next;
    
};
