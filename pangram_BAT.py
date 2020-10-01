def checkPangram(s):
   lst = []
   for i in range(26):
      lst.append(False)
   for c in s.lower(): 
      if not c == " ":
         lst[ord(c)-ord('a')]=True
   for ch in lst:
      if ch == False:
         return False
   return True
# Driver Program 
str1=input("Enter The String ::7gt;")
if (checkPangram(str1)):
   print ('"'+str1+'"')
   print ("is a pangram")
else:
   print ('"'+str1+'"')
   print ("is not a pangram")
