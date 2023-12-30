class QuickSelect:
    def __init__(self):
        pass
        
    def quickselect(self, arr, low, high, k):
        if low == high:
            return arr[low]

        i = self.partition(arr, low, high)
        if k == i:
            return arr[k]
        elif k < i:
            return self.quickselect(arr, low, i - 1, k)
        else:
            return self.quickselect(arr, i + 1, high, k)


    def partition(self, arr, low, high):
        pivot = arr[high][1]
        i = low
        for j in range(low, high):
            if arr[j][1] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]

        return i


class MaxSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.mx_tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, idx, left, right):
        if left == right:
            self.mx_tree[idx] = self.arr[left]
            return self.mx_tree[idx]
        else:
            m = (left + right) // 2
            l = self.build(idx * 2 + 1, left, m)
            r = self.build(idx * 2 + 2, m + 1, right)
            self.mx_tree[idx] = max(l, r)
            return self.mx_tree[idx]
            
    def _query(self, idx, left, right, start, end):
        # start & end are query range
        # left & right are tree idx range
        # [start, left, right, end]
        if left >= start and right <= end:
            return self.mx_tree[idx]
        else:
            l = 0
            r = 0
            m = (left + right) // 2
            if m >= start:
                l = self._query(idx * 2 + 1, left, m, start, end)
            if m + 1 <= end:
                r = self._query(idx * 2 + 2, m + 1, right, start, end)
            return max(l, r)

    def query(self, start, end):
        return self._query(0, 0, self.n - 1, start, end)

    def _update(self, idx, left, right, start, end, val):

        if left == right:
            self.mx_tree[idx] =  val
            return self.mx_tree[idx]
        else:
            l = -float('inf')
            r = -float('inf')
            m = (left + right) // 2 
            if m >= start:
                l = self._update(idx * 2 + 1, left, m, start, end, val)
            if m + 1 <= end:
                r = self._update(idx * 2 + 1, m + 1, right, start, end, val)

            self.mx_tree[idx] = max(l, r)
            return self.mx_tree[idx]
    
    def update(self, start, end, val):
        self._update(0, 0, self.n - 1, start, end, val)


class InverseFactor:
    def __init__(self, mx = 10 ** 5, mod = 10 ** 9 + 7):
        self.mx = mx
        self.mod = mod
        self.fac = [0] * (mx + 1)
        self.invFac = [0] * (mx + 1)

    def _fastpow(self, a, b, mod):
        ans = 1
        while b:
            if b & 1:
                ans = ans * a % mod
            a = (a * a) % mod
            b = b >> 1

        return ans
        
    def build(self):
        self.fac[1] = 1
        # build factorization
        for i in range(2, self.mx + 1):
            self.fac[i] =  i * self.fac[i - 1] % self.mod
        self.invFac[-1] = self._fastpow(self.fac[-1], self.mod - 2, self.mod)
        
        # build inverse factor
        for i in range(self.mx, 0, -1):
            self.invFac[i - 1] = self.invFac[i] * i % self.mod
        
