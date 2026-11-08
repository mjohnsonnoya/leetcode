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
    const dummy = new ListNode();
    let curr = dummy;
    let carry = 0;
    while (l1 !== null || l2 !== null || carry !== 0) {
        const val1 = (l1 !== null) ? l1.val : 0;
        const val2 = (l2 !== null) ? l2.val : 0;

        const sum = (val1 + val2 + carry) % 10;

        curr.next = new ListNode();
        curr = curr.next;

        curr.val = sum;

        carry = Math.floor((val1 + val2 + carry) / 10);

        if (l1 !== null) {
            l1 = l1.next;
        }

        if (l2 !== null) {
            l2 = l2.next;
        }
    }

    return dummy.next;
};
