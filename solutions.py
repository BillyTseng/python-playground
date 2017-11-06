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
# Case 1: empty source or empty target
s = ""
t = ""
print "Question 1 case 1 should be False: {}".format(question1(s, t))

# Case 2: source is shorter than target.
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
