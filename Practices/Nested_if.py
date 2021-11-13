#What is the score?
score = int(input("What is your test score?: "))
if score >= 90:
    print("your grade is an A.")

else:
    if score >=80:
        print ("your grade is a b")
    else:
        if score >= 70:
            print("Your grade is a c")
        else:
            if score >=60:
                print("your score is d")
            else:
                print("your grade is an f.")