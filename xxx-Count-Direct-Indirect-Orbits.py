'''
orbit =['Sun)B','B)C','C)D','C)H','B)F'].

Find the total number of direct or indirect orbits.
For example, in this orbital diagram, D directly revolves around C, because C directly revolves around B, so
D indirectly revolves around B, and also indirectly around SUN, D has a total of 3 orbits, and C has 2 orbits.
'''

orbits_list = ['OCM>B', 'B>C', 'C>D', 'D>E', 'B>F', 'D>H']

# node_list is a list of node which has orbits
node_list = {}
for orbit in orbits_list:
    start, end = orbit.split('>')
    if start not in node_list:
        node_list[start] = [end]
    else:
        node_list[start].append(end)

# count direct orbitz
direct_count = 0
for node in node_list:
    direct_count += len(node_list[node])

print(direct_count)

# dfs for all orbits, level=1 means it directly revoles around 'OCM' or 'Sun' 
def dfs(node_list, root, level):
    if not root or root not in node_list:
        return 0
    res = len(node_list[root]) * level
    for node in node_list[root]:
        res += dfs(node_list, node, level + 1)
    return res

total_count = dfs(node_list, 'OCM', 1)
print(total_count)
