from graph_business_trip.graph import *


def graph_business_trip(graph,arr):
    cost=0
    state=False

    for city in range(len(arr)-1):
        neighbors=graph.get_neighbors(arr[city])
        for i in neighbors:
           if arr[city+1]==i.node:
               cost+=i.weight
               state=True
      
    if state==False:
        cost=0
        state=False
        return f'{state},${cost}'


    return f'{state},${cost}'


if __name__=="__main__":
    g=Graphs()
    a=g.add_node('a')
    b=g.add_node('b')
    c=g.add_node('c')

    g.add_edge(a,b,5)
    g.add_edge(b,c,4)  
    g.add_edge(c,a,3)
    g.add_edge(b,a,1)

    print(graph_business_trip(g,[a,b]))


    