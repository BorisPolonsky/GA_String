import GA_String
a=GA_string()
L=[]
str1="TooYoungTooSimpleSometimesNaive"
str2=""
a.Set_target(str1)

for i in range(3000):
    while(len(L)<40):
        L.append(a.spam(len(str1)))
    L=a.Fixed_Ratio_Individual_Selection(L,0.5)
    L+=a.single_gene_mutation(L,0.5,True)
    L=a.Sort_Individual(L,True)
    if str2!=L[0]:
        str2=L[0]
        print(str2)
    if str2==str1:
        break

#Here goes the test
