print("Это викторина на знание географии. Ответь на вопросы и узнай, насколькo хорошо ты в ней разбираешься !")

question1 = "Какая столица франции?"
question2 = "Какая самая длинная река в мире?"
question3 = "Какой океан самый большой?"
question4 = "Какое самое твердое природное вещество на Земле?"
question5 = "В какой стране расположены древние пирамиды Гизы?"
true_answer1 = "Париж"
true_answer2 = "Амазонка"
true_answer3 = "Тихий океан"
true_answer4 = "Алмаз"
true_answer5 = "Египет"
score = 0
total_score = 0
answer1 = input(question1)
if answer1 == "Париж":
  total_score = score + 1

else:
  total_score = score + 0
answer2 = input(question2)
if answer2 == "Амазонка":
  total_score = score + 1

else:
  total_score = score + 0
answer3 = input(question3)
if answer3 == "Тихий океан":
  total_score = score + 1

else:
  total_score = score + 0
answer4 = input(question4)
if answer4 == "Алмаз":
  total_score = score + 1

else:
  total_score = score + 0
answer5 = input(question5)
if answer5 == "Египет":
  total_score = score + 1

else:
  total_score = score + 0

if total_score >= 3:
 print("Вы набрали много баллов! Вас можно считать экспертом")
else:
  print("Вы набрали не очень много баллов. Расширяйте свой кругозор, вам есть, куда стремиться")

print("Вы набрали", total_score, "баллов")
