import string
import socket
import os
def main():
    result = open("/home/output/result.txt", "w+")

    path = "/home/data"
    dir_list = os.listdir(path)
    result.write("Files in ")
    result.write(path)
    for x in dir_list:
        result.write(" \n")
        result.write(x)

    IF_file = open('/home/data/IF.txt','r')
    data = IF_file.read()
    word_IF_file=data.split()

    Lime_file = open('/home/data/Limerick.txt','r')
    data = Lime_file.read()
    word_Lime_file=data.split()
    result.write(" \n")
    result.write(" Number of words present in Limerick: "+str(len(word_Lime_file)))
    word_IF=[]
    for i in word_IF_file:
        jo=i.translate(str.maketrans('', '', string.punctuation))
        jo=jo.capitalize()
        word_IF.append(jo)
    result.write(" \n")
    result.write(" Number of words present in IF: "+str(len(word_IF)))
    result.write(" \n")
    result.write(" Total number of words present in both the files: "+str(len(word_IF) + len(word_Lime_file)))
    count_IF = []
    set1 = set(word_IF)

    for i in set1: 
        count_IF.append(word_IF.count(i))

    word_IF = list(set(word_IF))
    order_count_IF= sorted(count_IF,reverse=True)
    result.write("\n")
    result.write("List the top 3 words with maximum number of counts in IF")
    j=0
    for j in range(0,3):
         for i in range(0,len(count_IF)):
             if(count_IF[i]== order_count_IF[j]):
                 result.write("\n")
                 result.write(""+word_IF[i]+" - "+ str(count_IF[i]) )
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    result.write("\n")
    result.write("IP Address of machine is:" + IPAddr) 
    result.close()
    result_file = open('/home/output/result.txt','r')
    data_result = result_file.read()
    print(data_result)
if __name__ == "__main__":
    main()
