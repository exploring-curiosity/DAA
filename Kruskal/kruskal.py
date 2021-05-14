MAX=1000

class UndirectedEdge:
  def __init__(self,v,w,weight):
    self.v=v
    self.w=w
    self.weight=weight
  def Weight(self):
    return int(self.weight)
  def From(self):
    return self.v
  def to(self):
    return self.w
  
class UnionFind:
  parent=[]
  size=0
  def __init__(self,size):
    self.size=size
    for i in range(0,size):
      self.parent.append(-1)

  def find(self,ind):
    while(self.parent[ind]!=-1):
      ind=self.parent[ind]
    return ind

  def Union(self,x,y):
    x_parent=self.find(x)
    y_parent=self.find(y)
    self.parent[y_parent]=x_parent

class WeightedUndiGraph:
  v=[]
  e=[]
  adj_mat=[]
  n=0
  def __init__(self,n):
    for i in range(0,n):
      temp=[]
      self.n=n
      for j in range(0,n):
        if(i==j):
          temp.append(0)
        else:   
          temp.append(MAX)
      self.adj_mat.append(temp)

  def EdgeUndirectedGraph(self):
    for i in range(0,self.n):
      self.v.append(input("Enter Vertex:"))
    total=int(input("Enter total edges: "))
    for i in range(0,total):
      v,weigh,w=input("Enter From Weight To:").split()
      weigh=int(weigh)
      temp=UndirectedEdge(v,w,weigh)
      self.add_edge(temp)
  
  def V(self):
    return len(self.v)
  
  def E(self):
    return len(self.e)
  
  def findIndex(self,v):
    pos=-1
    for i in range(0,self.V()):
      if(self.v[i]==v):
        pos=i
        return pos
    return pos

  def add_edge(self,edge):
    self.e.append(edge)
    print(edge.From(),"--",edge.Weight(),"--",edge.to())
    from_pos=self.findIndex(edge.From())
    to_pos=self.findIndex(edge.to())
    self.adj_mat[from_pos][to_pos]=edge.Weight()
    self.adj_mat[to_pos][from_pos]=edge.Weight()

  def adj(self,v):
    pos=findIndex(v)
    if(pos==-1):
      return
    edges=[]
    for i in range(0,self.E()):
      if(self.e[i].From()==v):
        edges.append(self.e[i])
    return edges

  def edges(self):
    return self.e
        

class kruskal:
  size=0
  graph1=None
  uf=None
  edges=[]
  def __init__(self,size,g1):
    self.size=int(size)
    self.uf=UnionFind(size)
    self.graph1=g1
    self.edges=self.graph1.e
  def sortEdges(self):
    for i in range(0,self.graph1.E()):
      min_ind=i
      for j in range(i+1,self.graph1.E()):
        if(self.edges[min_ind].Weight()>self.edges[j].Weight()):
          min_ind=j
      self.edges[i],self.edges[min_ind]=self.edges[min_ind],self.edges[i]
        
  def KruskalAlgo(self):
    self.sortEdges()
    ind=0
    T=[]
    while(len(T)!=self.size-1):
      temp=self.edges[ind]
      from_pos=self.graph1.findIndex(temp.From())
      to_pos=self.graph1.findIndex(temp.to())
      if(self.isCycle(from_pos,to_pos)!=1):
        self.uf.Union(from_pos,to_pos)
        T.append(temp)
      ind=ind+1
    return T

  def isCycle(self,x,y):
        x_parent=self.uf.find(x)
        y_parent=self.uf.find(y)
        if(x_parent==y_parent):
          return 1
        return 0
  
graph1=WeightedUndiGraph(5)
graph1.EdgeUndirectedGraph()
krusk=kruskal(5,graph1)
MST=krusk.KruskalAlgo()
print("The edges which form the MST:-")
for i in range(0,len(MST)):
  print(MST[i].From(),"--",MST[i].Weight(),"--",MST[i].to())


'''
input:-
a
b
c
d
e
7
a 1 b
e 2 d
b 3 d
b 4 e
b 5 c
d 6 c
c 7 a
output:-
The edges which form the MST:-
a -- 1 -- b
e -- 2 -- d
b -- 3 -- d
b -- 5 -- c
'''
