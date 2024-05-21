/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int leng(ListNode* head) {
        if (head == NULL){
            return 0;
        }
        return leng(head->next) + 1;
    }
    ListNode* skip(ListNode* head, int n) {
        if (n == 0) {
            return head;
        }
        return skip(head->next, n - 1);
    }
    ListNode* sortList(ListNode* head, int len = -1) {
        if (len == -1){
            len = leng(head);
        }
        if (len == 0) {
            return NULL;
        }
        if (len == 1) {
            return head;
        }
        ListNode* l1end = skip(head, len / 2 - 1);
        ListNode* l2begin = l1end->next;
        l1end->next = NULL;
        ListNode* l1 = sortList(head, len / 2);
        ListNode* l2 = sortList(l2begin, len - len / 2);
        ListNode* last = NULL;
        ListNode* ret = NULL;
        int i = 0;
        while (l1 != NULL && l2 != NULL && i < len) {
            if (l1->val < l2->val) {
                if(last)last->next = l1;
                last = l1;
                l1 = l1->next;
            } else {
                if(last)last->next = l2;
                last = l2;
                l2 = l2->next;
            }
            if (!ret) {
                ret = last;
            }
            ++i;
        }
        if (l1 != NULL) last->next = l1;
        if (l2 != NULL) last->next = l2;
        return ret;
    }
};
