#HW by Shadi Bdair
num=int(input("Enter a number: "))
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            }
if num < 10:
    print(num2words[num].capitalize())
elif num >= 10 and num < 100:
    sum=int(num / 10) + int(num % 10)
    print(num,"it's two digit,  sum is:",sum)
if num <= 1000 and num >=100:
    ahadot= int (num % 10)
    asarot=int( num / 10) %10 
    meoot= int(num / 100)
    print(num,"it's three digits, mul is:",(meoot*asarot)*ahadot)
if num >= 1000:
    print(num,"number has more than 3 digits")

    
