# Description: The program is used to take data from the text files salesIDs and salesdata and displays the respective quarter.
# The prpogram also displays the maximum sales which shows the salesperson who sold the most and the amount.
# It also displays the quarter in which the sales were maximum and its amount. 

# Author: HARSH GUPTA

def getIDs(filename): # Defintion of the function called getIDs that declares 2 lists and extrats data from the text files.

    # Declares the list named as id_list(for getting the data from salesIDs.txt) and sales_data(for getting the data from salesdata.txt)
    id_list=[]
    sales_data=[]
    
    file = open(filename,'r') # Opens the file and opens it to read the content from the file
    
    for line in file: # Starts the for loop in order to strip all the content to the lists.
        # The for loop goes line by line in the program.
        
        id_list.append(line.strip()) 
        sales_data.append([0.0,0.0,0.0,0.0])
        
    file.close() # Closes the text file.
    id_list.sort() # Used to sort the ID numbers in the list
    
    return id_list,sales_data # Returns the values of the id_list and sales_data. 

def process_sales_data(filename, id_list, sales_data): # Definition of the function process_sales_data 
    
    file=open(filename,'r') # Opens the file and opens it to read the content from the file
    
    for line in file: # Starts the for loop in order to assign all the values in the respective quarter.
        # The for loop goes line by line in the program.
        
        line=line.strip().split() # It takes the values from each line 

        sales_id=line[0] 
        sales_val=int(line[1])
        # This alots the quarters for each of the values 
        if sales_val>=1 and sales_val<=3:
            quarter=0
        elif sales_val>=4 and sales_val<=6:
            quarter=1
        elif sales_val>=6 and sales_val<=9:
            quarter=2
        else:
            quarter=3

        amount = float(line[2]) 
        location=id_list.index(sales_id) 
        
        sales_data[location][quarter] = round((sales_data[location][quarter]+amount),3) # Gets the value for each sales in each quarter and rounds the value.
        
    file.close() # Closes the text file.
    
    return sales_data # Returns the value for sales_data.


def print_report(id_list, sales_data): # Definition of the function in order to display the prices as per each quarter. 
    
    print('\n\n -------------Annual Sales Report-------------\n')
    print('\nID\t   QT1\t\t   QT2\t\t   QT3\t\t   QT4\t\t Total')

    # Declares the value for all the contents in each of the qaurters and also finds the value
    qtr1=0
    qtr2=0
    qtr3=0
    qtr4=0
    _id=0
    max_value=0

    # Starts a for loop in order to get all the values in the respective locations. 
    for sales in range(len(id_list)):
        # Giving the values for each quarters 
        qtr1=qtr1+sales_data[sales][0]
        qtr2=qtr2+sales_data[sales][1]
        qtr3=qtr3+sales_data[sales][2]
        qtr4=qtr4+sales_data[sales][3]
        
        total=round(sum(sales_data[sales]),3) # Calculates the total for each quarter and rounds the value accordingly.
        
        value=max([sales_data[sales][0],sales_data[sales][1],sales_data[sales][2],sales_data[sales][3]]) # Finds the maximum value in the sales. 

        if value>max_value:
            max_value=value
            max_id=id_list[sales] 

            # Prints the respective values from the text files and has been formatted to give the 
        print(id_list[sales],format(sales_data[sales][0],'8.2f'),format(sales_data[sales][1],'8.2f'),
              format(sales_data[sales][2],'8.2f'),format(sales_data[sales][3],'8.2f'),format(total,'8.2f'), sep='\t') 
        
        qtr_total=qtr1+qtr2+qtr3+qtr4 # Calculates the total of each quarter.
    
    print("Total", format(qtr1, '8.2f'), format(qtr2, '8.2f'), format(qtr3, '8.2f'), format(qtr4, '8.2f'),format(qtr_total, '8.2f'), sep='\t')
    amount=max([qtr1,qtr2,qtr3,qtr4]) # Prints the data as per each quarter for the respective
    
    location = [qtr1,qtr2,qtr3,qtr4].index(amount) 
    
    print('\nMax sales by Salesperson: ID =',max_id+', Amount = $'+str(round(max_value,3))) # Displays the the details for the salesperson with maximum sales.
    # It also displays the amount that was sold by the person. 
    print('Max sales by Quarter: Quarter = ',str(location+1)+', Amount = $'+str(round(amount,3))) # Dsiplays the maximum sale in the quarter.
    # It also displays the maximum amount for that particular quarter.

def main():

    # Asks the user to enter the sales ID file. 
    id_file_name=input('Enter the name of the sales ids file: ')
    id_list, sales_data=getIDs(id_file_name)

    # Asks the user to enter the sales data file.
    data_file_name=input('Enter the name of the sales data file: ')
    sales_data=process_sales_data(data_file_name, id_list, sales_data)

    print_report(id_list,sales_data)

main()

        
