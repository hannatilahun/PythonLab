
print("WELLCOME TO MY PROJECT")
print("              ")
print("              ")
print("NAME=HANNA"); 
print("              ")
print("              ")           
print("\t @@    @@      @@@@           @@@@         @@      @@@@         @@     @@@@    \t")
print("\t @@    @@     @@  @@         @@  @@       @@      @@  @@       @@     @@  @@   \t")
print("\t @@@@@@@@    @@@@@@@@       @@    @@     @@      @@    @@     @@     @@@@@@@@   \t")
print("\t @@    @@   @@      @@     @@      @@   @@      @@      @@   @@     @@      @@  \t")
print("\t @@    @@  @@        @@   @@        @@@@       @@        @@@@      @@        @@  \t")    
print("              ")
print("              ")
print("              ")
print("ID=0221") 
print("              ")
print("              ")                                      
print("\t @@@@@@@@       @@     @@       @@     @@      @@      \t")
print("\t @@    @@     @@ @@   @@      @@ @@   @@    @@@@@      \t")
print("\t @@    @@    @@  @@  @@      @@  @@  @@        @@       \t")
print("\t @@    @@   @@   @@ @@      @@   @@ @@         @@       \t")
print("\t @@@@@@@@  @@    @@@@      @@    @@@@       @@@@@@@@    \t")    
print("              ")
print("              ")
print("              ")


def char_frequency(str1):
    
    result = {}
    for letter in str1:
   
        if letter.isalpha() :
            count = str1.count(letter)
            result[letter] = count

    sortedCharResult = dict(sorted(result.items(), key=lambda x:x[1], reverse=True))
    for letter1,value in sortedCharResult.items():

        if value == 1:
            print(value,letter1,",", end="")
        else:
            print(value,letter1,"\'s,", end="")

print(char_frequency(input(" please Enter the String you want to test: ")))


