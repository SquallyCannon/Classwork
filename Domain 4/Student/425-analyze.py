def calculate_total(amount,license,tax=.08):
    total = (amount + license) * (1 + tax)
    return total
  
    
subtotal1 = calculate_total(19000,1000,.1) #22000
subtotal2 = calculate_total(19000,1000) #21600
print("The totals due are", subtotal1, "and", subtotal2)