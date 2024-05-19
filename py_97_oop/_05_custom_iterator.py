class Count:

    """Iterator that counts upwards forever"""

    def __init__(self, start=0, max_num=10):
        self.num = start
        self.max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        if num == self.max_num:
            raise StopIteration
        self.num += 1
        return num


for n in Count(max_num=42):
    print(n, end=" ")
