c = 0 
ch = 'y'
v = c = d = s = 0

while ch == 'y' or ch == 'Y':
    print("1. enter a string")
    print("2. check it is palindrome or not")
    print("3. create a string which is reverse of original string")
    print("4. print each word in reverse order")
    print("5. create a second string by removing all special characters from original string")
    print("6. remove all elements appearing for more than once")

    x = int(input("enter a choice: "))
    if x == 1:
        s = input("enter a string: ")
        print("entered string: ",s)

    if x == 2:
        l = len(s)
        j = l -1
        f = 0
        for i in range(l):
            if s[i] != s[j]:
                f = 1
                j = j - 1
            if f == 1:
                print("String is not a palindrome")
            else:
                print("String is palindrome")

    if x == 3:
        l = len(s) - 1
        sl = ""
        for i in range(l,-1,-1):
            sl = sl + s[i]
        print("reversed string is: ",sl)

    if x == 4:
        l = s.split()
        x = len(l)
        for i in l:
            for j in range(len(i)-1,-1,-1):
                print(i[j],end = "")

    if x == 5:
        st = ""
        for i in s:
            if (i >= 'A' and i <= 'Z') or (i >= 'a' or i <= 'z') or (i >= '0' and i <= '9'):
                st = st + 1
        print(st)

    if x == 6:
        st = ""
        for i in range(len(s)):
            c = s.count(s[i])
            if c == 1:
                st = st + s[i]
        print(s)

            
 ch = input("\n Do you want to continue y/n")

