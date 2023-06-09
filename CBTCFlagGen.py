import random

def main():
    
    def intro(): 
        print("Welcome to the CBTC Flag Generator!")
        print("This program will generate a flags for the PEs within your module as needed.")
        print("Please enter the number of flags that you would like to generate.")
    intro() 

    num_flags = int(input("Number of flags: "))       
 
    with open('flags.txt') as flag_file:
        flag_names = flag_file.read().split()
    
    if 1 <= num_flags <= 100:
        random_flags = random.sample(flag_names, k=num_flags)
        print("Flag names: ")
        for flag in random_flags:
            print(flag)
    else:
        print("Please enter a number between 1 and 100.")

    def export():
        print("Would you like to export these flags to a text file?")
        if input("Y/N: ").lower() == "y":
            with open('flag_export.txt', 'w') as export_file:
                for flag in random_flags:
                    export_file.write(flag + "\n")
            print("Flags exported to flag_export.txt")
        else:
            print("Flags not exported.")
    export()


main()

    
        

    

    
