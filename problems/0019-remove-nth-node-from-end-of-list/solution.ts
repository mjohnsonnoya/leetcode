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
    const dummy = new ListNode(undefined, head);
    const nodes: ListNode[] = [];

    nodes.push(dummy);

    let curr: ListNode | null = head;

    while (curr !== null) {
        nodes.push(curr);
        curr = curr.next
    }

    const length = nodes.length;

    nodes[length - n - 1].next = nodes[length - n + 1] ?? null;

    return dummy.next;
};
