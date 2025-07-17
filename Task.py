print("Welcome to Grading System!")
name = input("Enter Your name: ").capitalize()
print(f"Welcome {name}! Let's calculate your grade!")

marks = int(input("Kindly enter your marks (1-100): "))

if marks >=1 and marks <=100:
    #Marks more than 90 = grade A+
    if marks >= 90:
        print("Your grade is A+, OUTSTANDING ⭐!")
        print(f"{name}, you are now moving to the next class")
        print(f"{name}, you got 1st position")
    else:
         #Marks more than 85 and less than 90 = grade A
        if marks >= 85 and marks < 90:
            print("Your grade is A, WELL DONE 👏!")
            print(f"{name}, you are now moving to the next class")
            print(f"{name}, you got 2nd position")
        else:
            #Marks more than 80 and less than 85 = grade B+
            if marks >= 80 and marks < 85:
                print("Your grade is B+, IMPRESSIVE!")
                print(f"{name}, you are now moving to the next class")
                print(f"{name}, you got 2nd position")
            else:
                #Marks more than 75 and less than 80 = grade B
                if marks >= 75 and marks < 80:
                    print("Your grade is B, GOOD!")
                    print(f"{name}, you are now moving to the next class")
                    print(f"{name}, you got 3rd position")
                else:
                    #Marks more than 70 and less than 80 = grade C+
                    if marks >= 70 and marks < 75:
                        print("Your grade is C+, KEEP IT UP!")
                        print(f"{name}, you are now moving to the next class")
                        print(f"{name}, you got 3rd position")
                    else:
                        #Marks more than 65 and less than 70 = grade C
                        if marks >= 65 and marks < 70:
                            print("Your grade is C, GOOD JOB!")
                            print(f"{name}, you are now moving to the next class")
                            print(f"{name}, you got 3rd position")
                        else:
                            #Marks more than 60 and less than 65 = grade D+
                            if marks >= 60 and marks < 65:
                                print("Your grade is D+")
                                print(f"{name}, you are now moving to the next class")
                                print(f"{name}, you got 3rd position")
                            else:
                                #Marks more than 55 and less than 60 = grade D
                                if marks >= 55 and marks < 60:
                                    print("Your grade is D")
                                    print(f"{name}, you are now moving to the next class")
                                    print(f"{name}, but you need to focus more on studies!")
                                else:
                                    #Marks more than 50 and less than 55 = grade E
                                    if marks >= 50 and marks < 55:
                                        print("Your grade is E")
                                        print(f"{name}, you are now moving to the next class")
                                        print(f"{name}, but you need to focus more on studies!")
                                    else:
                                        #Marks less than 50 = grade F
                                        if marks < 50:
                                            print("Your grade is F")
                                            print(f"{name}, you will remain in the same class")
                                            print(f"{name}, work harder 🥲!")

else:
    print("Please Enter valid marks!")