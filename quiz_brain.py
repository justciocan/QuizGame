class QuizBrain:

    """ Initializes a new instance of the QuizBrain class """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions = q_list

    """ Receives a question from the question list and prompts it to the player"""
    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? : ")
        self.check_answer(user_answer, current_question.answer)

    """ Returns True if there are more questions in the list, False otherwise"""
    def still_has_questions(self):
        return self.question_number < len(self.questions)

    """ Function to check if a question has been answered correct"""
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You've got it right!")
        else:
            print(f"The correct answer is {correct_answer}.")
            print(f"You've got it wrong!")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")

    def final_words(self):
        print("You finished the quiz!")
        print(f"Your final score is {self.score}/{self.question_number}.")
        print("Thank you for playing!")