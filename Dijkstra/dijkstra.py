MAX=1000
class Heap:
        array=[]
        size=0
        def __init__(self):
                self.array=[['inti',-1]]

        def insert(self,key,item):
                self.size=self.size+1
                temp=[key,item]
                self.array.append(temp)
                i=len(self.array[1:])
                while(i>0):
                        if(self.array[i][1]<self.array[i//2][1]):
                                self.array[i],self.array[i//2]=self.array[i//2],self.array[i]
                        i=i//2
    
        def deleteMin(self):
                if(self.size==1):
                        return
                len1=len(self.array)-1
                value=self.array[1]
                self.array[1]=self.array[len1]
                self.rearrange()
                self.array=self.array[:len1]
                return value

        def rearrange(self):
                i=1
                while((2*i)+1<len(self.array)):
                    if(self.array[2*i][1]<self.array[i][1] or self.array[(2*i)+1][1]<self.array[i][1]):
                        if(self.array[2*i][1]<self.array[(2*i)+1][1]):
                            self.array[i],self.array[2*i]=self.array[2*i],self.array[i]
                            i=i*2
                        else:
                            self.array[i],self.array[(2*i)+1]=self.array[(2*i)+1],self.array[i]
                            i=(2*i)+1
                    else:
                        i=i*2
        
        def decreaseKey(self,key,dist):
                for i in range(1,len(self.array)):
                        if(self.array[i][0]==key):
                                self.array[i][1]=dist
                self.rearrange()
             
        def print_heap(self):
                for i in range(1,len(self.array)):
                        print(self.array[i][0])

class DirectedEdge:
        def __init__(self,v,w,weight):
                self.v=v
                self.w=w
                self.weight=weight
        def Weight(self):
             return self.weight
        def From(self):
                return self.v
        def to(self):
                return self.w

class WeightedDigraph:
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
        def EdgeWeightedDigraph(self):
                for i in range(0,self.n):
                        self.v.append(input("Enter vertex:"))
                total=int(input("Enter total edges:"))
                for i in range(0,total):
                        v=input("Enter from:")
                        w=input("Enter to:")
                        weigh=int(input("Enter weight:"))
                        temp=DirectedEdge(v,w,weigh)
                        self.add_edge(temp)
                
        def V(self):
                return len(self.v)
        def E(self):
                return len(self.e)
        def add_edge(self,edge):
                self.e.append(edge)
                from_pos=-1
                print(edge.From(),"--",edge.Weight(),"-->",edge.to())
                for i in range(0,len(self.v)):
                        if(edge.From()==self.v[i]):
                                from_pos=i
                                break
                to_pos=-1
                for i in range(0,len(self.v)):
                        if(edge.to()==self.v[i]):
                                to_pos=i
                                break
                self.adj_mat[from_pos][to_pos]=edge.Weight()

        def adj(self,v):
                pos=-1
                for i in range(0,len(self.v)):
                        if(self.v[i]==v):
                                pos=i
                                break
                if(pos==-1):
                        return
                edges=[]
                for i in range(0,len(self.e)):
                        if(self.e[i].From()==v):
                                edges.append(self.e[i])
                return edges

        def edges(self):
                return self.e

class SP:
        dist=[]
        size=0
        v_id=[]
        minheap=Heap()
        def __init__(self,G,s):
                self.G=G
                self.v_id=G.v
                pos=self.findIndex(s)
                self.size=len(self.v_id)
                for i in range(0,len(self.v_id)):
                        if(i==pos):
                                self.dist.append([self.v_id[i],0])
                        else:
                                self.dist.append([self.v_id[i],MAX])
                        self.minheap.insert(self.v_id[i],self.dist[pos][1])

        def findIndex(self,v):
                pos=-1
                for i in range(0,len(self.v_id)):
                        if(self.v_id[i]==v):
                                pos=i
                                return pos
                return pos
        def relax(self,e):
                f=self.findIndex(e.From())
                t=self.findIndex(e.to())
                w=e.Weight()
                self.dist[t][1]=self.dist[f][1]+w
                self.minheap.decreaseKey(e.to(),w)

        def tense(self,e):
                f=self.findIndex(e.From())
                t=self.findIndex(e.to())
                w=e.Weight()
                if(self.dist[f][1]+w<self.dist[t][1]):
                        return True
                else:
                        return False

        def findMin(self):
                min1=self.minheap.deleteMin()
                return min1[0]

        def dijkstra(self):
                for i in range(0,self.size):
                        min1=self.findMin()
                        edges=self.G.adj(min1)
                        for j in edges:
                                if(self.tense(j)):
                                        self.relax(j)
                print(self.dist)
                

'''
        def distTo(self,v):

        def hasPathTo(self,v):

        def pathTo(self,v):

'''

edge_arr=[]
graph=WeightedDigraph(4)
graph.EdgeWeightedDigraph()
sp=SP(graph,'v1')
sp.dijkstra()

'''
Enter vertex:v1
Enter vertex:v2
Enter vertex:v3
Enter vertex:v4
Enter total edges:5
Enter from:v1
Enter to:v3
Enter weight:1
v1 -- 1 --> v3
Enter from:v3
Enter to:v4
Enter weight:3
v3 -- 3 --> v4
Enter from:v4
Enter to:v2
Enter weight:4
v4 -- 4 --> v2
Enter from:v3
Enter to:v2
Enter weight:2
v3 -- 2 --> v2
Enter from:v1
Enter to:v2
Enter weight:5
v1 -- 5 --> v2
[['v1', 0], ['v2', 3], ['v3', 1], ['v4', 4]]
'''
