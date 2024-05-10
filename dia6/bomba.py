from time import sleep

lista = list(range(0, 11))
lista.reverse()

for i in lista:
    print(i)
    sleep(0.75)
    if i == 0:
        print("""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
        """)
