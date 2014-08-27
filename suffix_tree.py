__author__ = 'Joshua Chin'

def build_suffix_tree(string):
    '''a partially working implementation of based off the stackoverflow answer at
    http://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english/9513423#9513423'''
    root = {}
    active_node = root
    active_edge = None
    active_length = 0
    remainder = 1
    end = len(string)

    for index, char in enumerate(string):
        previous_node = None
        if not remainder:
            remainder = 1
        while remainder:
            print(char, active_edge, active_length, remainder, active_node is root) #debug

            if not active_length: #at node
                if char not in active_node:
                    active_node[char] = (index, end, {})
                else:
                    active_edge = char
                    active_length += 1
                    remainder += 1
                break
            
            else:
                active_link = active_node[active_edge]
                active_edge_length = active_link[1] - active_link[0]
                if active_edge_length == active_length: #detect if at an end of edge
                    active_node = active_link[2]
                    active_edge = None
                    active_length = 0
                    continue
                
                active_char = string[active_node[active_edge][0] + active_length]
                
                if char == active_char: #same character
                    active_length += 1
                    remainder += 1
                    break
                else: #different character, insertion

                    old_link = active_node[active_edge]

                    new_start = index - active_length
                    new_end = index
                    other_index = old_link[0]+active_length

                    new_node = {}
                    new_node[char] = (index, end, {})
                    new_node[string[other_index]] = (other_index, old_link[1], old_link[2])
                    
                    if previous_node is not None:
                        previous_node['suffix'] = new_node
                    previous_node = new_node

                    active_node[active_edge] = (new_start, new_end, new_node)

                    if active_node is root:
                        active_edge = string[new_start + 1]
                        active_length -= 1
                        remainder -= 1
                    else:
                        if 'suffix' in active_node:
                            active_node = active_node['suffix']
                        else:
                            active_node = root
    return root


x = build_suffix_tree('abcabxabcd')

