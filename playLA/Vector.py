class Vector:
    def __init__(self, lst):
        self._values = lst

    def __add__(self, other):
        assert len(self) == len(other), \
            "两个向量的维度不相等."
        return Vector([a + b for a, b in zip(self, other)])

    def __iter__(self):
        # 返回向量的迭代器
        return self._values.__iter__()

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
