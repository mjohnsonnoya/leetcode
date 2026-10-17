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
    const nodes: ListNode[] = [];

    const dummy = new ListNode(undefined, head);

    let curr = dummy;

    while (curr !== null) {
        nodes.push(curr);

        curr = curr.next;
    }

    let length = nodes.length;

    nodes[length - n - 1].next = nodes[length - n].next;

    return dummy.next;


};
