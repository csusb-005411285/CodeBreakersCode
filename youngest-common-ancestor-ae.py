#https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor
# This is an input class. Do not edit.
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	# find depth of both descendents
	depth_desc_one = get_depth(descendantOne)
	depth_desc_two = get_depth(descendantTwo)
	# if the depth of both descendents are same 
	if depth_desc_one == depth_desc_two:
		return find_common_ancestor(descendantOne, descendantTwo)
	else:
		# then the descendent with a higher depth should be on level with
		# the descendent with a lower depth
		diff = 0
		if depth_desc_one > depth_desc_two:
			diff = depth_desc_one - depth_desc_two 
		else:
			diff = depth_desc_two - depth_desc_one
		if depth_desc_one > depth_desc_two:
			    new_descendent = get_descendent_on_lower_depth(descendantOne, diff)
			    return find_common_ancestor(new_descendent, descendantTwo)
		else: 
			    new_descendent = get_descendent_on_lower_depth(descendantTwo, diff)
			    return find_common_ancestor(descendantOne, new_descendent)

def get_depth(descendant):
    depth = 0
    while descendant: #n
	    descendant = descendant.ancestor
	    depth += 1
    return depth

def find_common_ancestor(descendant_one, descendant_two):
    while descendant_one != descendant_two: #n
        if descendant_one:
			descendant_one = descendant_one.ancestor
        if descendant_two:
			descendant_two = descendant_two.ancestor
    return descendant_one
  
def get_descendent_on_lower_depth(descendent, diff):
    while diff > 0: #n
        descendent = descendent.ancestor
        diff -= 1
    return descendent

# 2nd attempt
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.	
	depth_one = get_depth(descendantOne)
	depth_two = get_depth(descendantTwo)
	desc_higher_depth = None
	desc_lower_depth = None
	descendent_on_same_level = None
	# compare the depths
	# store the descendent that has the higher depth
	if depth_one > depth_two:
		diff = depth_one - depth_two
		desc_higher_depth = descendantOne
		desc_lower_depth = descendantTwo
		# from the descendent of having higher depth, get the descendent which is on the same level as the other descendent
		descendent_on_same_level = get_descendent_on_same_level(desc_higher_depth, diff)
	else:
		diff = depth_two - depth_one	
		desc_higher_depth = descendantTwo
		desc_lower_depth = descendantOne
		# from the descendent of having higher depth, get the descendent which is on the same level as the other descendent
		descendent_on_same_level = get_descendent_on_same_level(desc_higher_depth, diff)
	# now since both the descendents are on the same level
	common_ancestor = find_common_ancestor(desc_lower_depth, descendent_on_same_level)
	# return the common ancestor
	return common_ancestor

def get_depth(descendent):
	# keep looping until you reach the top node
	depth = 0
	while descendent.ancestor:
		descendent = descendent.ancestor
		depth += 1
	return depth

def get_descendent_on_same_level(desc_higher, depth):
	desc = desc_higher
	while depth != 0:
		desc = desc.ancestor
		depth -= 1
	return desc

def find_common_ancestor(desc_left, desc_right):
	# traverse until you find a common ancestor
	while desc_left is not desc_right and desc_left and desc_right:
		desc_left = desc_left.ancestor
		desc_right = desc_right.ancestor
	return desc_left
   
