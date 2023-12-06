#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_a_lm(s):
        return (s if s != search else replace)
    return list(map(s_a_lm, my_list))
