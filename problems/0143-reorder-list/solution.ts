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

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    let slow = head;
    let fast = head;

    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let curr: ListNode | null = slow.next;
    slow.next = null;

    let secondHalf: ListNode | null = null;

    while (curr !== null) {
        const next = curr.next;
        curr.next = secondHalf;
        secondHalf = curr;
        curr = next;
    }

    let firstHalf: ListNode | null = head;

    while (secondHalf !== null) {
        const firstNext = firstHalf.next;
        const secondNext = secondHalf.next;

        firstHalf.next = secondHalf;
        secondHalf.next = firstNext;

        firstHalf = firstNext;
        secondHalf = secondNext;
    }

};
