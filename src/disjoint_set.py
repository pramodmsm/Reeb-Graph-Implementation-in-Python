class Disjoint_set():


    def __init__(self,n : int):
        self.n = n 
        self.parent = list(range(self.n))
        self.rank = [0 for x in range(self.n)]

    def find(self,x : int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x : int,y : int):
        x_root = self.find(x)
        y_root = self.find(y)
        print('parent array before union :',self.parent)
        print(x_root,y_root)
        if x_root == y_root:
            return
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            print('parent array after union :',self.parent)
        else:    
            self.parent[x_root] = y_root
            print('parent array after union :',self.parent)
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root]+=1
    
    def print_parents(self):
        print('index :',list(range(self.n)))
        print('parent :',self.parent,sep='')
    

if __name__ == '__main__':
    # Part a)
    uf = Disjoint_set(10)
    uf.union(2,1)
    uf.union(4,3)
    uf.union(6,5)
    uf.union(2,4)
    print("\nParent array after union(2,1), union(4,3) and union(6,5):")
    uf.print_parents()  

