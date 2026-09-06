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
    let slow: ListNode = head;
    let fast: ListNode = head;

    while (fast.next !== null && fast.next.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    let second = slow.next;
    slow.next = null;

    let prevNode = null;

    while (second !== null) {
        let next = second.next;
        second.next = prevNode;
        prevNode = second;
        second = next;
    }

    // 1, 2
    // 5, 4 ,3

    let first = head;
    let secondHalf = prevNode;

    while (secondHalf !== null) {
        let firstNext = first.next;
        let secondNext = secondHalf.next;

        first.next = secondHalf;
        secondHalf.next = firstNext;

        first = firstNext;
        secondHalf = secondNext;
    }


};
