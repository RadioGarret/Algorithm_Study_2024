def preorder_dfs(node):
    if not node:
        return

    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)
    return




def inorder_dfs(node):
    if not node:
        return 
    
    inorder_dfs(node.left)
    print(node.val)
    inorder_dfs(node.right)
    return