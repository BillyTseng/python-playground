#! /usr/bin/env python
"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return
a boolean True or False.
"""


def question1(s, t):
    """
    arg:
        s: source string.
        t: target string.
    return:
        True: target is a substring of source.
        False: target is not a substring of source.
    """
    # the edge cases: empty string and source is shorter than target.
    if not s or not t or len(s) < len(t):
        return False
    else:
        # Store counts of upper and lower case of alphabets for the source.
        s_map = [0] * 52
        hashmap_helper(s_map, s)

        # Store counts of upper and lower case of alphabets for the target.
        t_map = [0] * 52
        hashmap_helper(t_map, t)

        # Find matched string.
        for char in t:
            if t_map[ord(char) % 52] is not s_map[ord(char) % 52]:
                return False

        return True


def hashmap_helper(hashmap, string):
    """
    arg:
        hashmap: store counting values in a list.
        string: incoming input string.
    """
    for char in string:
        hashmap[ord(char) % 52] += 1


# Test cases of question 1:
# Case 1: edge case, empty source or empty target
s = ""
t = ""
print "Question 1 case 1 should be False: {}".format(question1(s, t))

# Case 2: edge case, source is shorter than target.
s = "aa"
t = "bbb"
print "Question 1 case 2 should be False: {}".format(question1(s, t))

# Case 3: Udacity and ad.
s = "Udacity"
t = "ad"
print "Question 1 case 3 should be True: {}".format(question1(s, t))

# Case 4: Google and oo.
s = "Google"
t = "OOgl"
print "Question 1 case 4 should be False: {}".format(question1(s, t))

"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""


def question2(string):
    return palindrome_helper(string)


def palindrome_helper(string):
    # the edge cases: empty string and one char string.
    if len(string) <= 1:
        return string
    elif string[0] == string[-1]:
        middle_str = palindrome_helper(string[1:-1])
        return string[0] + middle_str + string[-1]
    else:
        begin_str = palindrome_helper(string[1:])
        end_str = palindrome_helper(string[:-1])
        if len(begin_str) >= len(end_str):
            return begin_str
        else:
            return end_str


# Test cases of question 2:
# Case 1: edge case, empty string.
print "Question 2 case 1 should be empty string: {}".format(question2(""))

# Case 2: edge case, one char string.
print "Question 2 case 2 should be A: {}".format(question2("A"))

# Case 3: race13car11
print "Question 2 case 3 should be rac3car: {}".format(
                                                    question2("race13car11"))

# Case 4: 8884321123777
print "Question 2 case 4 should be 321123: {}".format(
                                                    question2("8884321123777"))

"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G.
"""


def question3(G):
    sorted_list = sort_nodes_by_weight(G)
    # Because of undriected graph, need to divide 2
    # the least number of edge will be number of vertex - 1
    if len(sorted_list)/2 > (len(G) - 1):
        sorted_list = sorted_list[:(len(G) - 1)*2]

    sorted_list = transfer_to_graph(sorted_list)
    return sorted_list


def sort_nodes_by_weight(G):
    """
    sort_nodes_by_weight sort nodes of graph, G, by ascending order in weight.
    arg: G as inputed graph.
    return: a list of nodes which is sorted by edge's weight.
    """
    nodes = []
    for k, v in G.items():
        if len(v) == 1:
            nodes.append([k, v[0][0], v[0][1]])
        else:
            for i in v:
                nodes.append([k, i[0], i[1]])

    nodes = sorted(nodes, key=lambda item: item[2])
    return nodes


def transfer_to_graph(input_list):
    """
    transfer_to_graph exchange list to graph.
    arg: inputed list
    return: graph
    """
    graph = {}
    for item in input_list:
        if item[0] not in graph.keys():
            graph[item[0]] = []
        graph[item[0]].append((item[1], item[2]))

    return graph


# Test cases of question 3:
# Case 1: edge case, empty graph.
print "Question 3 case 1 should be empty graph: {}".format(question3({}))

# Case 2: edge case, it is already a minimum spanning tree.
G = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print "Question 3 case 2 should be "
print "{'A': [('B', 2)],"
print " 'C': [('B', 5)],"
print " 'B': [('A', 2), ('C', 5)]}}: {}".format(question3(G))

# Case 3
G = {'A': [
    ('B', 2), ('C', 1)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5), ('A', 1)]}

print "Question 3 case 2 should be "
print "{'A': [('C', 1), ('B', 2)],"
print " 'C': [('A', 1)],"
print " 'B': [('A', 2)]}}: {}".format(question3(G))
