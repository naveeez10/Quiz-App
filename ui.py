from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.now_score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20 ,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(150,125,text="hehe",
        width = 280 ,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        self.score_label = Label(text=f"Score : {self.now_score}")
        self.score_label.grid(row=0,column=1)
        self.score_label.config(bg=THEME_COLOR,fg="black")

        true_img = PhotoImage(file="images/true.png")
        self.true_butt = Button(image=true_img,highlightthickness=0,command=self.true_butt_pressed)
        self.true_butt.grid(row=2,column=0)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_butt = Button(image=false_img,highlightthickness=0,command=self.false_butt_pressed)
        self.false_butt.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
            self.canvas.configure(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)

    def true_butt_pressed(self):
        user_answer = self.quiz.check_answer("True")
        if user_answer:
            self.now_score += 1
        self.give_feedback(user_answer)
    
    def false_butt_pressed(self):
        user_answer = self.quiz.check_answer("False")
        if user_answer:
            self.now_score += 1
        self.give_feedback(user_answer)

    def give_feedback(self,is_right : bool) :
        self.score_label.config(text= f"Score : {self.now_score}")
        if is_right:    
            self.canvas.configure(bg="Green")
        else:
            self.canvas.configure(bg="Red")
        self.canvas.after(500,self.get_next_question)

