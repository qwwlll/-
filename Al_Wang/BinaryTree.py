from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#### leetcode 94 105 106 450 889
### 二叉树先序<->树的先根<->森林的先序
### 二叉树中序<->树的后根<->森林的中序



### leetcode 94 中序遍历 Binary Tree
class Solution:
    def inorderTraversal(self , root ):
        # write code here
        res = []
        def inorder(root):    ###dfs 思想递归
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

### 前序：
def qianxuTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
### 后序：
def houxuTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

### other way：
### 手写
class Solution:
    def inorderTraversal(self , root ):
        # write code here
        res, stack = [], []
        cur  = root
        while stack or cur:
            if cur :
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
            
### 前中后三序遍历
class Solution:
    def threeOrders(self , root: TreeNode) -> List[List[int]]:
        # write code here
        res = [[],[],[]]
        def dfs(root):
            if not root: return None
            res[0].append(root.val) ## 前： 根左右
            dfs(root.left)
            res[1].append(root.val) ## 中： 左根右
            dfs(root.right)
            res[2].append(root.val) ## 后： 左右根
        dfs(root)
        return res

### leecode 145 后序 
### leetcode 144 前序
### leetcode 94 中序

                



###leetcode 98. 验证二叉搜索树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
##### 100 检验 树是否相等
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


### leetcode 101. 对称二叉树
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return check(p.right, q.left) and check(p.left, q.right)
        return check(root.right, root.left)

### leetcode 102. 二叉树的层序遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = [root]
        while que:
            lenth = len(que)
            level = []
            for i in range(lenth):
                node = que.pop(0)
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(level)
        return res
### leetcode 104 二叉树的最大深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        a = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return a

### leetcode 105 通过中序和前序建树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        def recurBu(inorder):
            x = preorder.pop(0)
            node = TreeNode(x)
            inx  = inorder.index(x)
            left_l = inorder[:inx]
            right_l = inorder[inx+1:]
            if left_l:
                node.left = recurBu(left_l)  
            if right_l:
                node.right = recurBu(right_l)
            return node
        return recurBu(inorder)
### leetcode 106 通过后序和中序建树
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        def build(inorder):
            x = postorder.pop(-1)
            idx = inorder.index(x)
            node = TreeNode(x)
            left_l = inorder[:idx]
            right_l= inorder[idx + 1:]
            if right_l:
                node.right = build(right_l)
            if left_l:
                node.left = build(left_l)
            return node
        return build(inorder)



### leetcode 107. 二叉树的层序遍历 II
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res =[]
        if not root:
            return []
        que = [root]
        while que:
            level = []
            for i in range(len(que)):
                node = que.pop(0)
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(level)
        return res[::-1]



### leetcode 108 数组构建BST
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bulid(left, right):
            if left > right:
                return None

            mid  = (left + right) >> 1
            root = TreeNode(nums[mid])
            root.left = bulid(left, mid - 1)
            root.right = bulid(mid + 1, right)
            return root

        return bulid(0, len(nums)-1)

### leetcode 109 链表造BST

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMid(left, right):
            fast, slow, = left, left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow
        def bulidTree(left, right):
            if left == right:
                return None
            mid = getMid(left, right)
            root = TreeNode(mid.val)
            root.left = bulidTree(left, mid)
            root.right = bulidTree(mid.next, right)
            return root
        return bulidTree(head, None)



#### leetcode 110 判断是否平衡
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        if abs(height(root.right) - height(root.left) ) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False



#### leetcode 114 BST转链表
class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr


