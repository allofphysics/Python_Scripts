class saw():
    def __init__(self,l,w):
        self.l = l
        self.w = w
        self.score = 0 
        self.geneSet = ''.join([str(x) for x in range(1,l*w+1)])
        self.parent = ''.join([str(x) for x in range(1,l*w+1)])
        self.bestFitness = 0
    
    def create_transition_dic(self):
        transition_dic={}
        num_tiles=self.l*self.w
        for n in range(1,num_tiles+1):
            adjacent_edges_list=[]
            if ((n-1)%self.w != 0): 
                adjacent_edges_list.append(n-1) # left
            if (n% self.w     != 0): 
                adjacent_edges_list.append(n+1) # right
            if (n > self.w):
                adjacent_edges_list.append(n-self.w) 
            if (n<=((self.w*self.l)-self.w)):
       
                adjacent_edges_list.append(n+self.w) # bottom
            transition_dic[n]=adjacent_edges_list
        return transition_dic
    
    def solution_correct_length(self):
        if len(list(self.parent)) < (self.l * self.w):
            return False
        elif len(list(self.parent)) == len(set(self.parent)):
            return True
        
    def possible_solution(self):
        self.score = 0
        dct = self.create_transition_dic()
        solution = list(self.parent)
        for ix in range(len(solution)-1):
            #print ix
            src = int(solution[ix])
            dst = int(solution[ix+1])
            if dst in dct[src]:
                self.score += 1
                pass
            else:
                return False
        if self.solution_correct_length():
            self.score +=1
            return True
        
    def get_fitness(self):
        self.possible_solution()
        return self.score
    
    def mutate(self):
        index = random.randrange(1,len(self.parent))
        childGenes = list(self.parent)
        newGene,alternate = random.sample(self.geneSet,2)
        if newGene == childGenes[index]:
            childGenes[index] = alternate
        else:
            childGenes[index] = newGene
        return ''.join(childGenes)
    
    def update_parent(self):
        print self.parent
        print self.bestFitness
        parent = self.parent
        self.parent = self.mutate()
        score = self.get_fitness()
        print 'score',score
        if score < self.bestFitness:
            self.parent = parent
        else:
            self.bestFitness = score
