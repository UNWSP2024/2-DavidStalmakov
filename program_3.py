def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    # then displays the subtotal of the sale,
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.
    item1 =float(input("Enter the price of item one: "))
    item2 =float(input("Enter the price of item two: "))
    item3 =float(input("Enter the price of item three: "))
    item4 =float(input("Enter the price of item four: "))
    item5 =float(input("Enter the price of item five: "))
    # Calculate Subtotal
    subtotal = item1 + item2 + item3 + item4 + item5
    #calculate sales tax
    sales_tax=subtotal*0.07
    #calculate total
    total=subtotal+sales_tax
    #Results
    print("Subtotal: ",format(subtotal,".2f"), sep="")
    print("Sales Tax: ",format(sales_tax,".2f"), sep="")
    print("Total: $", format(total,".2f"), sep="")
calculate_total_purchase()

