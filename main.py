#Alannah steck
#U2L1
#mutliplacation table 

# ONE LINE - NO MORE, NO LESS

table = [numOne * numTwo for numOne in range(1,11) for numTwo in range(1,11)]

########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################