 #!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This functiontells the user if they're able to date my grand daughter

def main():
    # This functiontells the user if they're able to date my grand daughter
    
    # input
    
    age_string = input("Enter your age: " )
    print("")
    
    
    #process
    try:
        age_number = int(age_string)
        if age_number > 25 and age_number < 40:
            print("You're acceptable to date my grandchild.")
        else:
                if age_number < 25:
                    print("You're too young.")
                if age_number > 40: 
                    print("You're too old.")
    except Exception:
        print("{0} is an invalid input.".format(age_string))
        
    print("\nDone.")
    

if __name__ == "__main__":
    main()
    