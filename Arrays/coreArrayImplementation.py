class fundamentalArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        if self.length == 0:
            return None
        lastItem = self.data[self.length - 1]    
        del self.data[self.length -1]
        self.length -= 1
        return lastItem
    
    def delete(self, index:int):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self, index: int):
        if (index == self.length -1):
            del self.data[index]
            self.length -= 1

        for item in range(index, self.length):
            if (item == self.length -1):
                del self.data[item]
                return
            self.data[item] = self.data[item+1]
            




    
newArray = fundamentalArray()
newArray.push("hi")
newArray.push("you")
newArray.push("are")
newArray.push("nice")

print(newArray.data)
# newArray.pop()
#print(newArray.data)
newArray.delete(1)
print(newArray.data)
