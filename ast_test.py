#https://greentreesnakes.readthedocs.io/en/latest/manipulating.html
import ast
class FuncLister(ast.NodeVisitor):
    lst = []
    def visit_FunctionDef(self, node):
        resp = ((node.__dict__['lineno'],node.__dict__['col_offset'],'def',node.name))
        self.lst.append(resp)
        #print(resp)
        self.generic_visit(node)
    def visit_Call(self, node):
        dct = node.__dict__['func'].__dict__
        if 'id' in dct.keys():
            resp = ((dct['lineno'],dct['col_offset'],'call',dct['id']))
            self.lst.append(resp)
        elif 'value' in dct.keys():
            dct_v1  = dct['value'].__dict__
            if 'id' in dct_v1.keys():
                resp = ((dct_v1['lineno'],dct_v1['col_offset'],'call',dct_v1['id']))
                self.lst.append(resp)
        self.generic_visit(node)
    
    def output_DataFrame(self):
        import pandas as pd 
        df = pd.DataFrame(self.lst)
        df.columns = ['line_no','col_offset','type','name']
        return df
    
from sys import argv
f = open(argv[1])
data  = f.read()
f.close()
tree = ast.parse(data)

X = FuncLister()
X.visit(tree)
df = X.output_DataFrame()
print(df)
df.to_csv('sample.csv',index=False)

