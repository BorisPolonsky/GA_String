import random
class GA_string():
    default_dict_set={"Latin":list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),"Default":list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ~!@#$%^&*()_+`1234567890-={}|:\"<>?[]\\;',./")}
    def Fitness_Score(self,origin_Lst,target):
        l=len(target)
        Fitness_Score=[]
        for individuals in origin_Lst:
            if l!=len(individuals):
                Fitness_Score.append(-1)
            else:
                Matched_ch_num=0
                for i in range(l):
                    if individuals[i]==target[i]:
                        Matched_ch_num+=1
                Fitness_Score.append(float(Matched_ch_num)/float(l))
        return(Fitness_Score)

    def Set_origin(self,origin):
        if (type(origin)==str):
            self.str_origin=origin

    def Set_target(self,target):
        if (type(target)==str):
            self.str_target=target
    def Set_dic(self,dic_type):
        if type(dic_type)==list:
            self.dic=dic_type[:]
        elif type(dic_type)==str:
            self.dic=self.default_dict_set[dic_type]
    def GetDict(self):
        return(self.dic)
    def single_gene_mutation(self,individual_Lst,mutation_rate,filter_non_mutant=False):
        mutant_Lst=[]
        if(type(mutation_rate)==float):
            for individual in individual_Lst:
                if(random.random()<=mutation_rate):
                    gene_individual=list(individual)
                    gene_individual[random.randint(0,len(gene_individual)-1)]=self.dic[random.randint(0,len(self.dic)-1)]#bug
                    mutant_Lst.append("".join(gene_individual))
                elif filter_non_mutant==False:
                    mutant_Lst.append(individual)
        elif type(mutation_rate)==list:
            for index_individual in range(len(individual_Lst)):
                if(random.random()<=mutation_rate[index_individual]):
                    gene_individual=list(individual)
                    gene_individual[random.randint(0,len(gene_individual)-1)]=self.dic[random.randint(0,len(self.dic)-1)]#bug
                    mutant_Lst.append("".join(gene_individual))
                elif filter_non_mutant==False:
                    mutant_Lst.append(individual)
        return(mutant_Lst)

    def pairwise_crossover(self,Parent_1,Parent_2):
        gene_p1=list(Parent_1)
        gene_p2=list(Parent_2)
        if len(gene_p1)!=len(gene_p2):
            return(Parent_1,Parent_2)
        else:
            pos1=random.randint(0,len(gene_p1)-1)
            pos2=random.randint(0,len(gene_p1)-1)
            if(pos1>pos2):
                pos1,pos2=pos2,pos1
            #gene_p1[pos1:pos2],gene_p2[pos1:,pos2]=gene_p2[pos1:pos2],gene_p1[pos1:pos2]#Didn't know why it doesn't work...
            #substitution code:
            temp=gene_p1[pos1:pos2]
            gene_p1[pos1:pos2]=gene_p2[pos1:pos2]
            gene_p2[pos1:pos2]=temp
            return("".join(gene_p1),"".join(gene_p2))


    def Fixed_Ratio_Individual_Selection(self,individual_source,Ratio=0.5):
        Selected_Generation_Lst=individual_source[:]
        Selected_Generation_Lst=self.Sort_Individual(Selected_Generation_Lst,True)
        Num_Selected=int(len(Selected_Generation_Lst)*Ratio)
        Selected_Generation_Lst=Selected_Generation_Lst[0:Num_Selected-1]
        return(Selected_Generation_Lst)

    def Roulette_Individual_Selection(self,individual_source):
        Selected_Generation_Lst=[]
        Fitness_Score_Lst=self.Fitness_Score(individual_source,self.str_target)
        for i in range(len(individual_source)):
            if random.random()<=Fitness_Score_Lst[i]:
                Selected_Generation_Lst.append(individual_source[i])
        return(Selected_Generation_Lst)

    def spam(self,str_len):
        l=[]
        for i in range(str_len):
            l.append(self.dic[random.randint(0,len(self.dic)-1)])
        return("".join(l))

    def __init__(self):
        self.str_origin=""
        self.str_target=""
        self.Parents_Lst=[]        
        self.dic=[]
        self.Set_dic("Default")

    def Sort_Individual(self,individual_Lst,reversed=False):
        Fitness_Score_Lst=self.Fitness_Score(individual_Lst,self.str_target)
        str_score_structure_Lst=[]
        sorted_individual_Lst=[]
        for i in range(len(individual_Lst)):
            str_score_structure_Lst.append([individual_Lst[i],Fitness_Score_Lst[i]])
        str_score_structure_Lst=sorted(str_score_structure_Lst,key=lambda str_score_structure_Lst:str_score_structure_Lst[1],reverse=reversed)
        sorted_individual_Lst=list(map(lambda x:x[0],str_score_structure_Lst))
        return sorted_individual_Lst

    def getDic(self):
        return(self.dic)

