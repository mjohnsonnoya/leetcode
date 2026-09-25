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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let length = 0;
    let curr: ListNode | null = head;

    while (curr !== null) {
        length += 1;
        curr = curr.next;
    }

    let dummy = new ListNode(undefined, head);
    curr = dummy;

    for (let r = 0; r < length - n; r++) {
        curr = curr.next;
    }

    curr.next = curr.next.next;

    return dummy.next;
};
