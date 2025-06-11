#string is immutable ->cannot be edited
##denoted by - '' , "" , """"""
# '',"" are used for single line 
##""" """ are used for multi line

# ******************************************************************************

# name = "madhur"
# print(name)
# print(type(name))


# ####accessing methods in string
name = "  Madhur pvt "
# print(name.upper())# upper converts in upper case
# print(name.lower())# lower converts in lower case
# print(name.title())# capatilise first letter of all strings
# print(name.capitalize())# first character will be upper case and other will be lower case
# print(name.casefold())#convert all letter in lower case or in case less comparision
# print(name.swapcase())#convert uppercase to lower case or lower to upper
# print(name.strip())#for shifting
# print(name.lstrip())#left shifting 
# print(name.rstrip())#right shifting
# print(name.replace("pvt","set"))#for replacing with new but we have to tell it about new and old
# print(name.split("h"))#break the string
print(name.partition("h"))# gives output in three parts or more
print(name.startswith("M"))#starting letter is true or not
print(name.endswith("t"))#ending letter is true or not
print(name.isalpha())
print(name.encode())
print(name.encode("utf-8"))
print(name.encode("ascii"))
print(name.removeprefix("m"))
print(name.removesuffix("v"))
print(name.zfill(20))
print(name.center(20,"%"))
print(name.ljust(20,"%"))
print(name.rjust(20,"%"))



##### indexing and slicing
#indexing- accessing single character from the string
#slicing - accessing multiple character from the string

## h e l l o
## 0 1 2 3 4 - positive
##-5-4-3-2-1 - negative
#name = "madhur pvt"
# print(name[0])#>>>>>>>>>>>>>>>INDEXING>>>>>>>>>>>>>>>>
# print(name[-1])#>>>>>>>>>>>>>>>INDEXING>>>>>>>>>>>>>>>>

#slicing
#[start:end:step/skip]
#print(name[-3:])


#<<<<<<<<<<<<<<<<<<<<<<<<FORMATTED STRING>>>>>>>>>>>>>>>>>>>>>>>>>

# age  = 10
# #text = "my age is 10"+age
# text = f"my age is {age}"
# print(text)

# text = "my name is  \"jai\""# escape sequence
# print(text)

