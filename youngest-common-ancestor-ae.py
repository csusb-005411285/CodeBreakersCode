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
