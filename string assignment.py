import logging
logging.basicConfig(filename="string_logging.log",level="DEBUG",format= "%(levelname)s %(name)s %(asctime)s  %(message)s")
logging.info("we are creating the string class")
class string_file:
    s="this is My First Python Programming class and i am learNING python string and its function"
    logging.info("The string is= %s",s)
    def extract(self,s):
        try:
            logging.info("Try to extract data from index one to index 300 with a jump of 3")
            data=s[1:300:3]
            logging.info("the extracted data is ----> %s ",data)
            return data
        except Exception as e:
            logging.exception(e)

    def reverse(self,s):
        try:
            logging.info("Try to reverse a string without using reverse function")
            b=s[::-1]
            logging.info("the reverse string is----> %s",b)
            return b
        except Exception as e:
            logging.exception(e)

    def splitU(self,s):
        try:
            logging.info("Try to split a string after conversion of entire string in uppercase")
            c =s.upper()
            d = c.split()
            logging.info("The split string after converting in upper is----> %s",d)
            return d
        except Exception as e:
            logging.exception(e)

    def lower(self,s):
        try:
            logging.info("try to convert the whole string into lower case ")
            e=s.lower()
            logging.info("the string in lower case is----> %s",e)
            return e
        except Exception as e:
            logging.exception(e)

    def capital(self,s):
        try:
            logging.info("Try to capitalize the whole string")
            f=s.title()
            logging.info("the capitalize string is----> %s",f)
            return f
        except Exception as e:
            logging.exception(e)

    def replace_(self,s1,s2):
        try:
            logging.info("Replace a string charecter by another charector by taking your own example")
            j=s1.replace(s2," ")
            logging.info("the string after replacing the data is----> %s",j)
            return j
        except Exception as e:
            logging.exception(e)

    def cen(self):
        try:
            logging.info("Try  to give of string center function with and exmple")
            e1="rish"
            k = e1.center(20, "@")
            logging.info("the string is in center----> %s",k)
            return k
        except Exception as e:
            logging.exception(e)

string_operation=string_file()
print(string_operation.extract(string_operation.s))
print(string_operation.lower(string_operation.s))
print(string_operation.cen())
print(string_operation.splitU(string_operation.s))
print(string_operation.capital(string_operation.s))
print(string_operation.replace_("rishabh","abh"))
print(string_operation.reverse(string_operation.s))


