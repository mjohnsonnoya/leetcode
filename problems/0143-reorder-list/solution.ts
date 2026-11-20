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

    let second = slow.next;
    let prevNode: ListNode | null = null;

    slow.next = null;

    while (second !== null) {
        const secondNext = second.next;
        second.next = prevNode;
        prevNode = second;
        second = secondNext;
    }

    let firstHalf = head;
    let secondHalf = prevNode;

    while (secondHalf !== null) {
        const firstNext = firstHalf.next;
        const secondNext = secondHalf.next;

        firstHalf.next = secondHalf;
        secondHalf.next = firstNext;

        firstHalf = firstNext;
        secondHalf = secondNext;
    }
};
