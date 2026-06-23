/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* a=list1;
    struct ListNode* b=list2;
    struct ListNode* temp=
        (struct ListNode*)calloc(1, sizeof(struct ListNode));
    struct ListNode* cur = temp;
    while (a!=NULL && b!= NULL) {
        if (a->val <=b->val) {
            cur->next=a;
            cur=a;
            a=a->next;
        } else{
            cur->next=b;
            cur=b;
            b=b->next;
        }
    }
    if (a!= NULL) {
        cur->next=a;
    } else {
        cur->next=b;
    }
    return temp->next;
    
}