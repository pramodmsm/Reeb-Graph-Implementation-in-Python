class Vertex(object):
    '''a vertex object for every coordinates of the 
        object which is a .PLY file
        
        Args:
        index -> type int -> identifier of the vertex
        x,y,z -> coordinates of the  vertices 
    '''
    
    
    index:int
    x:int
    y:int
    z:int
    next = None
    parent = None

    def __init__(self,index,x,y,z):
        self.index = index
        self.x =  x
        self.y =  y
        self.z =  z

    def __lt__(self, v: object):
        return self.index < v.index
    
    