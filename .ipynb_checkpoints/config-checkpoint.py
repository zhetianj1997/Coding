List = list
from collections import defaultdict
import heapq
import time
from functools import lru_cache
from functools import cache
from typing import Optional

inf = float('inf')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TreeNodeBuild(arr, index = 0):
    if index >= len(arr) or arr[index] is None:
        return None
    else:
        return TreeNode(val = arr[index],
                        left = TreeNodeBuild(arr, index * 2 + 1),
                        right = TreeNodeBuild(arr, index * 2 + 2))

def TreePrint(tree):
    q = [tree]
    while q:
        # if all none, stop
        if len([t.val for t in q if t is not None]) == 0:
            break
        print([t.val if t is not None else None for t in q])
        tmp = []
        
        for i in range(len(q)):
            if q[i] is not None:
                tmp.append(q[i].left)
                tmp.append(q[i].right)
            else:
                tmp.append(None)
                tmp.append(None)
        q = tmp


    
def timing(func, r = 100):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        for i in range(r):
            result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to run")
        return result
    return wrapper


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

def ListNodeBuild(arr, index = 0):
    if len(arr) == 0:
        return None
    else:
        if index >= len(arr):
            return None
        else:
            return ListNode(val = arr[index], next = ListNodeBuild(arr, index + 1))