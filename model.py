import csv
import pandas as pd

path = 'finals.csv'

array = []

# Read the CSV file and populate the 2D array
with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row as a list to the 2D array
        array.append(row)

# CONSTANTS
    KAPPA = 1/1.606070856
    PR = 0.3268808347062054
    PS = 0.6731191652937946

    def _Omega(array, i):
        if str(array[i][42]) == 'NA':
            if (int(array[i][14]) == 1):
                return 0.7541335623792141
            else:
                return 0.529501332318233
        elif int(array[i][14]) == 1:
            return 0.7541335623792141 + (int(array[i][42])-119.59489826905558) / 119.59489826905558
        else:
            return 0.529501332318233 + (int(array[i][42])-99.3026113671275) / 99.3026113671275

            

    GR = 0.13454223363775925  
    GS = 0.8654577663622408
    T = 0.5

    SS = 0.5042735042735043 
    SR = 0.49572649572649574 
def calculate_flow(array,end_row = len(array)):
    n1 = end_row
    n2 = 0
    n3 = 0

    Pi = 0
    Gj = 0
    S = 0

    for i in range(1,end_row):
        server = int(array[i][13])
        winner = int(array[i][15])

        # For Points
        if n1==2:
            Pi/=2
            n1=1
        if winner == 1:
            if server == 1:
                Pi -= PS
            else:
                Pi -= PR
            Pi -= _Omega(array, i)
        else:
            if server == 1:
                Pi += PR
            else:
                Pi += PS
            Pi += _Omega(array, i)
        
        # For Games
        if int(array[i][18]) != 0:
            n2 += 1
            if int(array[i][18]) == 1:
                if server == 1:
                    Gj -= GS
                else: 
                    Gj -= GR
            else: 
                if server == 1:
                    Gj += GR
                else: 
                    Gj += GS                

        # For Sets
        if int(array[i][19]) != 0:
            n3 += 1
            if int(array[i][19]) == 1:
                if server == 1:
                    S -= SS
                else: 
                    S -= SR
            else: 
                if server == 1:
                    S += SR
                else: 
                    S += SS 
    if n2==0:
        n2 =1
    if n3 ==0:
        n3 = 1
    

    return KAPPA*(Pi/(2*n1)+Gj/n2+S/n3)
data = []
for i in range(2,len(array)):
    data.append(calculate_flow(array,i))

df = pd.DataFrame(data)
data_path = 'flow_final.csv'
df.to_csv(data_path, index = False)


