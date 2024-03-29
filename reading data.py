import csv
csv_file_path = '/Users/riyagoyal/Downloads/2024_MCM-ICM_Problems/Wimbledon_featured_matches.csv'

# Create an empty list to store the 2D array
data_2d_array = []
count = 0  # Counter variable for Model 1
returncount = 0  # Counter variable for Model 1
count3 = 7284  # Counter variable for Model 2
firstserve = 0  # Sum of first serve speeds for Model 2
secondserve = 0  # Sum of second serve speeds for Model 2
fscount = 0  # Counter for first serve speeds for Model 2
sscount = 0  # Counter for second serve speeds for Model 2

# Read the CSV file and populate the 2D array
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append the row as a list to the 2D array
        data_2d_array.append(row)

# Model 1: Serve and Return Rates
for i in range(1, 7285):
    if data_2d_array[i][13] == data_2d_array[i][15]:
        count += 1
    else:
        returncount += 1

serverate = count / 7284
returnrate = returncount / 7284
print("Serve Rate:", serverate)
print("Return Rate:", returnrate)

# Model 2: First Serve and Second Serve Averages
for i in range(1, 7285):
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

# Calculate average
fsaverage = firstserve / fscount
ssaverage = secondserve / sscount
# Display the resulting average
print("First Serve Average:", fsaverage)
print("Second Serve Average:", ssaverage)

# Model 3: Serve and Return Win Statistics

count_1 = 0  # Total points played on serve 1
count_2 = 0  # Total points played on serve 2
count1st = 0  # Number of wins made on first serve
count2nd = 0  # Number of wins made on second serve
countWin1 = 0  # Total speed on first serve
countWin2 = 0  # Total speed on second serve
win1count = 0  # Number of wins made on first serve with speed tracked
win2count = 0  # Number of wins made on second serve with speed tracked

for i in range(1, 7285):
    if int(data_2d_array[i][14]) == 1:
        if data_2d_array[i][13] == data_2d_array[i][15]:
            count1st += 1
            if data_2d_array[i][42].isdigit():
                countWin1 += int(data_2d_array[i][42])
                win1count += 1
        count_1 += 1
    else:
        if data_2d_array[i][13] == data_2d_array[i][15]:
            count2nd += 1
            if data_2d_array[i][42].isdigit():
                countWin2 += int(data_2d_array[i][42])
                win2count += 1
        count_2 += 1

print("Average for Serve 1:", count1st / count_1)
print("Average for Serve 2:", count2nd / count_2)
print("First Serve Win Speed Average", countWin1 / win1count)
print("Second Serve Win Speed Average", countWin2 / win2count)

# Model 4: Probability of Winning Game and Tiebreaker
def calculate_probability_of_winning_game(rate):
    return (
        rate**4 +
        4 * rate**4 * (1 - rate) +
        10 * rate**4 * (1 - rate)**2 +
        20 * rate**5 * (1 - rate)**3 / (1 - 2 * rate + 2 * rate**2)
    )

serverresult = calculate_probability_of_winning_game(serverate)
returnresult = calculate_probability_of_winning_game(returnrate)
print(f"The probability of winning the game when serving is: {serverresult}")
print(f"The probability of winning the game when returning is: {returnresult}")

tiebreak = (serverate + returnrate) / 2
print(f"The probability of winning the tiebreaker is: {tiebreak}")

# Model 5: Probability of Winning a Set when Serving or Returning First
keepcountserve = 0
keepcountreturn = 0
for i in range(1, 7285):
    if data_2d_array[i][4] != data_2d_array[i - 1][4]:
        store = int(data_2d_array[i][13])
    if int(data_2d_array[i][19]) != 0:
        if store == int(data_2d_array[i][19]):
            keepcountserve += 1
        else:
            keepcountreturn += 1

setserve = keepcountserve / (keepcountserve + keepcountreturn)
setreturn = keepcountreturn / (keepcountserve + keepcountreturn)
print("Probability of winning a set when serving first:", setserve)
print("Probability of winning a set when returning first:", setreturn)
