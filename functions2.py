def calculate_total(price , discount) :
    tax_Rate = 0.08
   

    tax  = price * tax_Rate
    final_Price = price +  tax - discount 

    print(f"Total : ${final_Price}")

calculate_total(price=40 ,  discount = 10)



