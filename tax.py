#_*_ coding: utf-8 _*_

def tax(age, pay, child) :
    tax_pay=0
    if 16 <= age or 65 >= age :
        if pay < 20000 :
            tax_pay = pay * 0.2

        else :
            tax_pay = pay * 0.5

    if child :
        tax_pay -= tax_pay *0.1

    return tax_pay
                
            
print tax(30, 10000, 1)

