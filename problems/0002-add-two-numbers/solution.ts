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
    let tail = dummy;
    let spill = 0;
    while (l1 !== null || l2 !== null || spill > 0) {
        const value = (l1?.val ?? 0) + (l2?.val ?? 0) + spill;
        const node = new ListNode(value % 10, undefined);
        tail.next = node;
        tail = node;
        spill = Math.floor(value / 10);
        if (l1 !== null) {
            l1 = l1.next;
        }

        if (l2 !== null) {
            l2 = l2.next;
        }
    }

    return dummy.next;
};
