"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1 :
        return x
    else:
        return foo(x-1)+foo(x-2)
    ### TODO
    pass

def longest_run(mylist, key):
    tracker = 0
    longest_count = 0
    for i in mylist:
        if (i > 0 and i==key):
            tracker += 1
            if tracker > longest_count:
                longest_count = tracker
    else:
        tracker = 0
    return count
    ### TODO
    pass

def longest_run(mylist, key):
    longest_count = 0
    temp_count = 0
    for i in mylist:
        if i == key:
            temp_count += 1
        else:
            temp_count == 1
    return longest_count


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if mylist[0] == key:
            fin = Result(1,1,1,True)
            return fin
        else:
            fin = Result(0,0,0,False)
            return fin
    else:
        mid = len(mylist)//2
        left = longest_run_recursive(mylist[:mid],key)
        right = longest_run_recursive(mylist[mid:],key)
        lr = left.right_size
        rl = right.left_size
        size = 0

        if lr!=0 and rl!=0:
            size = rl + lr
            if size > left.longest_size and size > right.longest_size:
                if left.is_entire_range and right.is_entire_range:
                    fin = Result(size,size,size,True)
                    return fin
                elif left.is_entire_range:
                    res = Result(size,right.right_size,size,False)
                    return fin
                elif right.is_entire_range:
                    fin = Result(left.left_size,size,size,False)
                    return fin
                else:
                    fin = Result(left.left_size,right.right_size,size,False)
                    return fin
        else:
               size = max(left.longest_size,right.longest_size)
               fin = Result(left.left_size,right.right_size,size,False)
               return fin

               ### TODO
               pass

print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12))


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
