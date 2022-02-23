class LRU:
    def find(self,key):
        i=0
        for el in self.data:
            if(el[0]==key):
                break
            i=i+1
        return i
    def __init__(self, capacity: int=10) -> None:
        self.capacity=capacity
        self.data=[]

    def get(self, key: str) -> str:
        i=self.find(key)
        if(i==len(self.data)):
            return ''
        self.data.append(self.data.pop(i))
        return self.data[len(self.data)-1][1]
    def set(self, key: str, value: str) -> None:
        i=self.find(key)
        if(i==len(self.data)):
            self.data.append([key,value])
            if(len(self.data)>self.capacity):
                self.data.pop(0)
        else:
            self.data[i][1]=value
    def rem(self, key: str) -> None:
        i=self.find(key)
        if(i<len(self.data)):
            self.data.pop(i)
