def unit_converter():
    print("🔄 Unit Converter")
    print("1. Centimeter →Meter")
    print("2. Meter → Km")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Exit")
    while True:
     choice=int(input("enter your choice:"))
     if choice==1:
         num=float(input("Enter Centimeter:"))
         cm=num*100
         print(f"Meters:{cm} cm")
     elif choice==2:
         num=float(input("Enter meter:"))
         m=num*1000
         print(f"kilometer:{m} m")
     elif choice==3:
         num=float(input("Enter celsius:"))
         cel=(num*9/5) + 32
         print(f"fre:{cel} °C")
     elif choice==4:
         num=float(input("Enter Fahrenheit:"))
         fah= (num - 32) * 5/9
         print(f"fahrenhit:{fah}°F")
     elif choice==5:
         print(exit)
         break
     else: print("invaild")
unit_converter()    