from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    try:
        new_quiz.next_question()

    except KeyboardInterrupt:
        print('Game Shutting Down, Good Bye')

new_quiz.final_words()
