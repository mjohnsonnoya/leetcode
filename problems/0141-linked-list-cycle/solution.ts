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

function hasCycle(head: ListNode | null): boolean {
    let slow: ListNode = head;
    let fast: ListNode = head;

    if (!head || !head.next) {
        return false;
    }

    slow = slow.next;
    fast = fast.next.next;


    while (fast !== null && fast.next !== null && slow != fast) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow == fast;

};
