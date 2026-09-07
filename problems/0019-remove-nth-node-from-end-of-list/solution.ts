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
    const prevNode = new ListNode();
    prevNode.next = head;

    let length = 0;
    let curr = head;

    while (curr !== null) {
        length += 1;
        curr = curr.next;
    }

    curr = prevNode;

    for (let i = 0; i < length - n; i++) {
        curr = curr.next;
    }

    curr.next = curr.next.next;
    return prevNode.next;
};
