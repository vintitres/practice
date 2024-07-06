/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/* 7

      7 
     / \
    3   15   <-3 (L)
        / \
        9  20
*/
class BSTIterator {
    stack<TreeNode*> back;
public:
    BSTIterator(TreeNode* root) {
        while (root->left) {
            back.push(root);
            root = root->left;
        }
        back.push(root);
    }
    
    int next() {
        TreeNode* r = back.top();
        back.pop();
        int v = r->val;
        if (r->right) {
            r = r->right;
            while (r->left) {
                back.push(r);
                r = r->left;
            }
            back.push(r);
        }
        return v;
        
    }
        
    bool hasNext() {
        return !back.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
