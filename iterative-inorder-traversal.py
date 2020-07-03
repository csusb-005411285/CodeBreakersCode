def iterativeInOrderTraversal(tree, callback):
	ptr = tree
    prev = None
	
	if not tree.left and not tree.right:
		callback(tree)
		return
    
    while ptr: # 1, 2, 4

        if prev is None:
            prev = ptr # 1

            if ptr.left: # 2
                ptr = ptr.left # 2
            elif ptr.right:
				callback(ptr)
                ptr = ptr.right
        
        elif prev is ptr.parent: # 2
            prev = ptr # 4

            if ptr.left:
                ptr = ptr.left

            elif ptr.right: # 
                callback(ptr) # 9
                ptr = ptr.right # 

            elif not ptr.left and not ptr.right:
                callback(ptr)
                ptr = ptr.parent

        # when current pointer is at the root and the prev pointer on the left 
        elif prev == ptr.left:
            callback(ptr)
			prev = ptr
			
            if ptr.right:
                ptr = ptr.right
            else:
                ptr = ptr.parent
        
        elif prev.parent == ptr:
			prev = ptr
            ptr = ptr.parent
