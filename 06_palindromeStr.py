st = input("Enter your string : ")

converted_str = st.replace(" ", "").lower()

#print (converted_str)

if converted_str == converted_str[::-1]:
    print ("Your string is palindrome")
else:
    print ("Your string is NOT palindrome")