 import pygraphviz as pgv


G=pgv.AGraph()

G=pgv.AGraph(strict=False,directed=True)

X = df.itertuples()

while True:
    resp = next(X)
    node_name = str(resp[1]) +'_'+ str(resp[2]) +'_'+ str(resp[4])
    G.add_node(node_name)
    n=G.get_node(node_name)
    if resp[3] == 'call':
        n.attr['color']='#8B0000'
    else:
        n.attr['color']='#1100FF'





G.layout()

G.draw('simple.png')
