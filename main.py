import tkinter as tk
import random


class Quiz:

  def __init__(self, master):
    self.master = master
    self.master.title("QUIZ")
    self.master.geometry('2000x2000')

    self.c = 0
    self.current_question = 0

    self.label_t = tk.Label(master, text="QUIZ", font=("arial", 50))
    self.label_t.place(x=600, y=50)

    self.label_u = tk.Label(master, text="Username", font=("arial", 30))
    self.label_u.place(x=250, y=250)

    self.entry = tk.Entry(master, font=("arial", 30))
    self.entry.place(x=500, y=250)

    self.questions = [{
        "question": "Which of them is a Keyword in Python?",
        "options": ["range", "def", "Val", "to"],
        "correct_option": 1
    }, {
        "question": "Which of the following is a built-in function in Python?",
        "options": ["factorial()", "print()", "seed()", "sqrt()"],
        "correct_option": 1
    }, {
        "question": "Which of the following is not a core datatype in Python?",
        "options": ["Tuple", "Dictionary", "Lists", "Class"],
        "correct_option": 3
    }, {
        "question":
        "Who developed the Python programming language?",
        "options": [
            "Wick Van Rossum", "Rasmus Lerdorf", "Guido Van Rossum",
            "Niene Stom"
        ],
        "correct_option":
        2
    }, {
        "question": "What is the extension for Python files?",
        "options": [".python", ".p", ".pl", ".py"],
        "correct_option": 3
    }]

    random.shuffle(self.questions)

    self.score_label = tk.Label(master, text="", font=("Arial", 30))
    self.score_label.place(x=800, y=100)

    self.button = tk.Button(master,
                            text="ENTER",
                            font=("arial", 30),
                            command=self.display_question)
    self.button.place(x=600, y=350)

  def display_question(self):
    if self.current_question < len(self.questions):
      question_info = self.questions[self.current_question]
      label_q = tk.Label(self.master,
                         text=f"Question {self.current_question + 1}",
                         font=("Arial", 35))
      label_q.place(x=550, y=50)
      label = tk.Label(self.master,
                       text=question_info["question"],
                       font=("Arial", 30))
      label.place(x=300, y=100)

      for i, option in enumerate(question_info["options"]):
        option_button = tk.Button(self.master,
                                  text=option,
                                  font=("Arial", 20),
                                  command=lambda i=i: self.check_answer(i))
        option_button.place(x=400 if i % 2 == 0 else 800,
                            y=200 + (i // 2) * 100)

      self.label_t.destroy()
      self.label_u.destroy()
      self.entry.destroy()
      self.button.destroy()
    else:
      self.show_final_score()

  def check_answer(self, selected_option):
    correct_option = self.questions[self.current_question]["correct_option"]

    if selected_option == correct_option:
      self.c += 1

    for widget in self.master.winfo_children():
      widget.destroy()

    self.current_question += 1
    self.display_question()

  def show_final_score(self):
    label_q6 = tk.Label(self.master, text="Total Score", font=("Arial", 38))
    label_q6.place(x=550, y=50)
    labell6 = tk.Label(self.master,
                       text=f"Correct Answers: {self.c}",
                       font=("Arial", 30))
    labell6.place(x=500, y=200)


if __name__ == "__main__":
  root = tk.Tk()
  quiz = Quiz(root)
  root.mainloop()
