leng_value = float(input("Please enter length: "))
leng_unit = str(input("Please enter the length unit: "))

if leng_unit == 'in' or leng_unit == '英寸':
    print('%f in = %f cm' % (leng_value, leng_value*2.54))
elif leng_unit == 'cm' or leng_unit =='公分':
    print('%f cm = %f in' % (leng_value, leng_value/2.54))
    