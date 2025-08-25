def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount = price * (discount_percentage/100)
        return price - discount
    else:
        return price
        
        
def user_input():
    price = float(input('Enter price. '))
    discount = float(input('Enter discount. '))
    print(f'The final price is #{calculate_discount(price, discount)}')
    
user_input()
