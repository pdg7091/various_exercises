# cover price on book is $24.95 but bookstores get a 40% discount
# shipping costs $3 for the first copy and 75cents for each additional copy
# what is the total wholesale cost for 60 copies

copies = 60
price = 24.95
wholesale = ((price) - (price * 0.4)) * copies
shipping = 3

if copies > 1:
    shipping += (0.75 * (copies - 1))

total = (round(wholesale + shipping, 2))

print(f'The total wholesale cost for 60 copies is ${total}.')
