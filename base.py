#1 Console 테스트
print("Test_1: " + "Hello World")

#2 File Open 테스트
file_name = "C:\sispromotion_log.txt"
try:
    file = open(file_name, "r")
    file_text = file.read()
    file.close()
    print("Test_2: " + file_text)
except IOError:
    print("Test_2: " + "Error to read " + file_name)
    
#3 Array 테스트
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for i in days:
    print("Test_3: " + i)
    
#4 Comment 테스트
#Test_4 설명을 시작하겠습니다.
'''
이 방식은 긴 주석을 설명하기 위하여 사용합니다.
C#에서는 /* */ 방식을 많이 사용하지요.
Python에서는 이러한 방식을 사용합니다.
'''

#5 변수 테스트
counter = 100
miles = 1000.0
name = "명호"

print("Test_5: " + str(counter)) #string으로 변환하고 싶을 때는 str(n)을 사용함.
print("Test_5: " + str(miles))
print("Test_5: " + name)

#6 변수 삭제 테스트
var1 = 1

del var1

try:
    print(var1)
except Exception:
    print("Test_6: " + "var1 was deleted.")
    
    
#7 char array 테스트

str = 'Hello World!'

print ("Test_7: " + str)          # Prints complete string
print ("Test_7: " + str[0])       # Prints first character of the string
print ("Test_7: " + str[2:5])     # Prints characters starting from 3rd to 5th
print ("Test_7: " + str[2:])      # Prints string starting from 3rd character
print ("Test_7: " + str * 2)      # Prints string two times
print ("Test_7: " + str + "TEST") # Prints concatenated string

#8 List 테스트

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print ("Test_8: " + list)          # Prints complete list
print ("Test_8: " + list[0])       # Prints first element of the list
print ("Test_8: " + list[1:3])     # Prints elements starting from 2nd till 3rd 
print ("Test_8: " + list[2:])      # Prints elements starting from 3rd element
print ("Test_8: " + tinylist * 2)  # Prints list two times
print ("Test_8: " + list + tinylist) # Prints concatenated lists

#9 Tuples 테스트
#Tuples란? List의 Read-only 버전이라고 생각하면 됨. ()로 변수를 감싸며 더 이상의 변수 업데이트가 불가능함.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

#10 Dictionary 테스트

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

#11 Decision Making 테스트
var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print ("Good bye!")
