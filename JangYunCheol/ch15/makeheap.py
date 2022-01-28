class MaxHeap:
    def __init__(self):
        self.item = [None]

    def __len__(self):
        return len(self.item) -1
    def _percolate_up(self):
        cur = len(self)

        parent = cur//2

        while parent>0:
            if self.item[cur]< self.item[parent]:
                self.item[cur] , self.item[parent] = self.item[parent], self.item[cur]


            cur =parent
            parent = cur//2

    def _percolate_down(self):
        pass

    def insert(self, k):
        self.item.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.item[1]
        self.item[1] = self.item[-1]
        self.item.pop()
        self._percolate_down(1)

        return root

def test_maxheap_we_made(lst, k):
    maxheap = MaxHeap()

    # for 문을 눈여겨봐두세요.
    # 힙정렬 시간복잡도 계산의 토대입니다.
    for elem in lst:
        maxheap.insert(elem)


assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1