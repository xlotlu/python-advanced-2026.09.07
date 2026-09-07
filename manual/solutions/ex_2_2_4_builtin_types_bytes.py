# Given the following string:
# greeting = "Добродошли на курс Питхон-а!"
# print its length
# encode it using utf-8 encoding and print the bytes object's length
# encode it using cp866 encoding and print the bytes object's length
# decode the bytes objects to string and check if the result is equal to the
# initial string

greeting = "Добродошли на курс Питхон-а!"
print(len(greeting))

utf8_greeting = greeting.encode("utf-8")
print(utf8_greeting, len(utf8_greeting))

cp866_greeting = greeting.encode("cp866")
print(cp866_greeting, len(cp866_greeting))

print(utf8_greeting.decode("utf-8") ==
      cp866_greeting.decode("cp866") ==
      greeting)
