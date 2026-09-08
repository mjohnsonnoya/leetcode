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

    while (fast.next !== null && fast.next.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let secondHalf = slow.next;
    slow.next = null;

    let prevNode: ListNode | null = null;

    while (secondHalf !== null) {
        const next = secondHalf.next;
        secondHalf.next = prevNode;
        prevNode = secondHalf;
        secondHalf = next;
    }

    let second = prevNode;
    let firstHalf = head;

    while (second !== null) {
        const secondNext = second.next;
        const firstNext = firstHalf.next;

        firstHalf.next = second;
        second.next = firstNext;

        firstHalf = firstNext;
        second = secondNext;
    }
};
