X = int(input('Enter the x = '))
Y = int(input('Enter the y = '))

if X > 0 and Y > 0:
    print("The point in the 1th quarter ")
elif X < 0 and Y > 0:
    print('The point in the 2nd quarter')
elif X < 0 and Y < 0:
    print('The point in the 3rd quarter')
elif X > 0 and Y < 0:
    print('The point in the 4th quarter')
else:
    print("It's the center of the coordinates")