import csv

# Replace 'your_csv_file.csv' with the actual path to your CSV file
csv_file_path = '/Users/riyagoyal/Downloads/2024_MCM-ICM_Problems/Wimbledon_featured_matches.csv'

# Create an empty list to store the 2D array
data_2d_array = []
count = 0
count3 = 7284
firstserve = 0
secondserve =0
fscount = 0
sscount = 0 

# Read the CSV file and populate the 2D array
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row as a list to the 2D array
        data_2d_array.append(row)

# Iterate over the rows and perform the desired calculations
for i in range(1, 7284):
#    if data_2d_array[i][13] == data_2d_array[i][15]:
        count += 1
        # Ensure that the value is convertible to an integer before adding
        if data_2d_array[i][42].isdigit():
            if int(data_2d_array[i][14]) == 1:
                firstserve += int(data_2d_array[i][42])
                fscount += 1
            else:
                secondserve += int(data_2d_array[i][42])
                sscount += 1
        else:
            count3 -= 1

# Calculate rate and average
rate = count / 7284
fsaverage = firstserve/fscount
ssaverage = secondserve/sscount
# Display the resulting rate and average
print("Rate:", rate)
print("First Serve Average:", fsaverage)
print("Second Serve Average:", ssaverage)

count_1 = 0 #total points played on serve 1
count_2 = 0 #total points played on serve 2
count1st =0 #number of wins made on first serve
count2nd =0 #number of wins made on second serve
countWin1 = 0 #total speed on first serve
countWin2 = 0 #total speed on second serve
win1count = 0 #number of wins made on first serve with speed tracked
win2count = 0 #number of wins made on second serve with speed tracked
for i in range(1, 7284):
    
    if int(data_2d_array[i][14]) == 1:
        if data_2d_array[i][13] == data_2d_array[i][15]:
            count1st += 1
            if data_2d_array[i][42].isdigit():
                countWin1 += int(data_2d_array[i][42]) 
                win1count +=1
        count_1 += 1
    else:
        if data_2d_array[i][13] == data_2d_array[i][15]:
            count2nd += 1
            if data_2d_array[i][42].isdigit():
                countWin2 += int(data_2d_array[i][42]) 
                win2count+=1
        count_2 += 1
        
print("Average for Serve 1:" , count1st/count_1)  
print("Average for Serve 2:", count2nd/count_2)  
print("First Serve Win Speed Average", countWin1/win1count)
print("Second Serve Win Speed Average", countWin2/win2count)



