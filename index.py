def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("\n\n##### Quiz App #####\n\n" "***All Questions 10 points each***")
ans = input("Are you ready to play (yes/no): ")
a ="***Note: write the full answer! do not write letter"
score = 0
total_questions = 4

correct_ans =["programmer", "mark zuckerberg", "robot", "bitcoin"]

if ans.lower() == "yes":
    print(a)
    print("\nQuestion- Who is the one who create software? ")
    give_options("Programmer", "Doctor", "Technician" )
    ans=input(">>>")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("\nQuestion- Who is the Founder of Facebook? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input(">>>")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("\nQuestion- What is a machine that can do human work called? ")
    give_options("Vehicle", "Robot", "Computer")
    ans = input(">>>")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("\nQuestion- What is a decentralized digital currency that you can buy, sell and exchange directly? ")
    give_options("Credit Card", "Bank", "Bitcoin")
    ans = input(">>>")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

i = score*10
if i < 30:
    print("Ouch, your score is ",i,"/ 40 better luck next time.")
elif i ==30:
    print("Nice! you scored ",i,"/ 40 you are quiet smart.")
else:
    print("Congratulations! it's a perfect ",i,"/ 40 you are Intelligent.")

