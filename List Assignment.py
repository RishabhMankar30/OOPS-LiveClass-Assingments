"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list
"""
import logging
logging.basicConfig(filename="list_logging.log",level="DEBUG",format="%(levelname)s %(asctime)s %(name)s %(message)s")
class list_operation:
    logging.info("we are in the list_operation class ")
    l=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
    logging.info("the given list is---> %s",l)

    def rev_lst(self,l):
        try:
            logging.info("Try to reverse a list")
            a=l[::-1]
            logging.info("The reverse list is---> %s",a)
            return a
        except Exception as e:
            logging.exception(e)

    def access_data234(self,l):
        try:
            logging.info("try to access 234 out of this list")
            logging.info("we are searching 234 in the list")
            t=[]
            for i in l:
                if type(i) == tuple:
                    for n in i:
                        if n == 234:
                            t.append(n)
                if type(i) == dict:
                    for j in i.keys():
                        if j == 234:
                            t.append(j)
            logging.info("The 234 is extracted from list--->%s",t)
            return t
        except Exception as e:
            logging.exception(e)
    def acess456(self,l):
        try:
            logging.info("access 456 from a list")
            for k in l:
                if type(k)==list:
                    for m in k:
                        if m==456:
                            logging.info("the 456 is extracted--> %s", m)
                            return m
        except Exception as e:
            logging.exception(e)
    def onlylst(self,l):
        try:
            logging.info("try to extract only a list from list")
            onlylist=[]
            for n in l:
                if type(n)==list:
                    onlylist.append(n)
            logging.info("The extracted list is--->%s",onlylist)
            return onlylist
        except Exception as e:
            logging.exception(e)
    def ext_sudh(self,l):
        logging.info("Extract string sudh from a list")
        try:
            for o in l:
                if type(o)==dict:
                    for p in o.values():
                        if p=="sudh":
                            logging.info("the string is extracted from a list---> %s", p)
            return p
        except Exception as e:
            logging.exception(e)

    def allkeys_values(self,l):
        try:
            keys=[]
            values=[]
            for q in l:
                if type(q)==dict:
                    for r in q.keys():
                        keys.append(r)
                    for v in q.values():
                        values.append(v)
            logging.info("all keys in dict is--->%s",keys)
            logging.info("all the values are--->%s",values)
            return keys,values
        except Exception as e:
            logging.exception(e)
list_obj=list_operation()

print(list_obj.onlylst(list_obj.l))
print(list_obj.access_data234(list_operation.l))
print(list_obj.allkeys_values(list_obj.l))
print(list_obj.rev_lst(list_obj.l))
print(list_obj.acess456(list_obj.l))
print(list_obj.ext_sudh(list_obj.l))
print(list_obj.allkeys_values(list_obj.l))





























