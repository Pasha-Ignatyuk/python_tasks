number_of_guests = int(input('enter number of guests'))
if number_of_guests < 20:
    print('home')
elif 20 <= number_of_guests <= 50:
    # сделал 50 включительно
    print('cofee')
else:
    print('restaurant')
