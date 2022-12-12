num_quarter = float(input('Enter quarter number: '))
if num_quarter == 1:
    print('Coordinate range: X > 0 and Y > 0')
elif num_quarter == 2:
    print('Coordinate range: X < 0 and Y > 0')
elif num_quarter == 3:
    print('Coordinate range: X < 0 and Y < 0')
elif num_quarter == 4:
    print('Coordinate range: X > 0 and Y < 0')
else:
    print('There is no quarter')
 
