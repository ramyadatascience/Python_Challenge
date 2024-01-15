import csv

with open('Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    print(csvreader)
    months=[]
    profit_loss =[]
    Changes =[]
    print("hello")
    csv_header = next(csvfile)
    print(csv_header)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        

    for c in range(len(profit_loss)):
         if c > 0:
             diff = profit_loss[c] - profit_loss[c-1]
             Changes.append(diff)

    length = len(Changes) 

    

# Calculate the Greatest Increase in profit
    Max_Profit = max(Changes)
    Max_Profit_idx = Changes.index(Max_Profit) + 1


# Calculate the Greatest decrease in profit
    Min_Profit = min(Changes)
    Min_Profit_idx = Changes.index(Min_Profit) + 1



# Calculate the Total
    total_Months = len(months) 
    pos_odd_sum = 0
    neg_sum = 0
  
    for num1 in profit_loss:
 
        # converting number
        # to integer explicitly
        # if negative number
        if(int(num1) < 0):
            # simply add
            # to the negative sum
            neg_sum = neg_sum + int(num1)
            # if positive number
        else:
            # add to positive odd sum
            pos_odd_sum = pos_odd_sum+int(num1)

    Total = pos_odd_sum + neg_sum

#Calculate the Average
    avg1 = round(sum(Changes[0:length]) / len(Changes),2)
    


#Display To the terminal
    Print_lines = []
    print(f"Financial Analysis")
    print(f"------------------")
    Print_lines.append("Financial Analysis")   
    Print_lines.append("------------------")

    print(f"Total months : ",total_Months)
    Print_lines.append("Total months :"+ str(total_Months))

    if Total > 0:
        print(f"Total : ${Total} ")
        Print_lines.append("Total : $"+str(Total))
    else:
        print(f"Total loss is -${Total} ")
        Print_lines.append("Total : -$"+str(Total))

   
    
    print(f"Average Change : ${avg1} ")
    Print_lines.append("Average Change : $"+str(avg1))

    
    
    print(f"Greatest Increase in Profits:{months[Max_Profit_idx]} ($ {Max_Profit})")
    print(f"Greatest decrease in Profits:{months[Min_Profit_idx]} ($ {Min_Profit})")
    Print_lines.append("Greatest Increase in Profits:"+str(months[Max_Profit_idx]+" ($ "+str(Max_Profit)+")"))
    Print_lines.append("Greatest decrease in Profits:"+str(months[Min_Profit_idx])+ " ($"+str(Min_Profit)+")")

#Writing to the out put file
with open("analysis/Financial_analysis.txt", "w") as file1:
    # Writing data to a file
    for i in Print_lines:
      file1.write("\n")
      file1.write(i)
      
    
     
