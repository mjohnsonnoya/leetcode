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

    const dummy: ListNode = new ListNode();
    let head = dummy;

    while (l1 !== null || l2 !== null || carry > 0) {

        const total = (l1?.val ?? 0) + (l2?.val ?? 0) + carry;

        const remainder = total % 10;

        head.next = new ListNode(remainder, undefined);

        carry = Math.floor(total / 10);

        if (l1 !== null) {
            l1 = l1.next;
        }

        if (l2 !== null) {
            l2 = l2.next;
        }

        head = head.next;
    }

    return dummy.next;
};
