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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    let dummy: ListNode = new ListNode(undefined, undefined);
    let curr = dummy;
    
    while(lists.some((element) => element !== null)) {
        let minVal = Infinity;
        let minIdx = -1;
        for (let i = 0; i < lists.length; i++) {
            let node = lists[i];
            if (node === null) {
                continue;
            }
            if (node.val <= minVal) {
                minVal = node.val;
                minIdx = i;
            }
        }

        let minNode = lists[minIdx]!;
        let minNodeNext = minNode.next;

        curr.next = minNode;
        curr = curr.next;
        lists[minIdx] = minNodeNext;
    }

    return dummy.next;
};
