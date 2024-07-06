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
class Solution {
    int _bstToGst(TreeNode* root, int extra) {
        if (root == NULL) {
            return 0;
        }
        int sumr = _bstToGst(root->right, extra);
        root->val += sumr + extra;
        int suml = _bstToGst(root->left, root->val);
        return root->val + suml - extra;
}
public:
    TreeNode* bstToGst(TreeNode* root) {
        _bstToGst(root, 0);
        return root;
    }
};
