from question import question
question_prompt=[
  "what color are Apples?\n(A) Red/Green \n(b)purple \n(c) orange\n \n",
  "what color are Bananas?\n(A) teal \n(b)Mangenta \n(c) yellow\n \n",
  "what color are strawberries?\n(A) Red/Yellow \n(b)Red \n(c) Blue\n \n",
]
questions=[
  question(question_prompt[0], "a"),
  question(question_prompt[1], "c"),
  question(question_prompt[2], "b"),
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got "+str(score)+"/" +str(len(questions)) + "correct")

run_test(questions)