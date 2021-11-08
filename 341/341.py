
from typing import List


class NestedIterator:
    def __init__(self, nestedList: List):
        self.stack = nestedList[::1]
    
    def next(self) -> int:
        return self.stack.pop().getIngeter()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False