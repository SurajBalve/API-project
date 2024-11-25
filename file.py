# f=open("poem.txt")
# print(f.read())
# f.close

# with open("poem.txt") as f:
    # print(f.read())
    
    
    
# f=open("poem.txt")
# c = f.read()
# if 'ChatGP' in c :
#     print("text is present :") 
    
# else :
#     print('text not present')
# f.close 

# f=open("poem.txt")
# c = f.read()
# if 'suraj' in c :
#     print("text is present :") 
    
# else :
#     print('text not present')
# f.close

# s= 'suraj'
# f=open("poem.txt","w")
# f.write(s)
# f.close
s=('sanket\n','manish\n','aniket\n')
with open("poem.txt","a") as f :
    f.writelines(s)
    