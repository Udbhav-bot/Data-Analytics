Ques = 'What is an Elephant'
oA="An insect"
oB="An reptile"
oC="An bird"
oD="A mammal"
correct = 'D'
print("welcome to the quiz")
print(Ques)
print('-'*20)
print(f'A.{oA}') #f-string
print(f'B.{oB}') #f-string
print(f'C.{oC}') #f-string
print(f'D.{oD}') #f-string
print('-'*20)

ans = input ('Enter your answer: ')
if ans.upper()== correct:
    print('Correct ✅')
else :
    print('Wrong❌')