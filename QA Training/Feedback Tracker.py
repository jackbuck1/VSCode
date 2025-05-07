import os

class DevOpsFeedback:
#This function allows the user to input the relevant data to give feedback on a student, based on the prompts given.
    def __init__(self):
        self.student_name = input ("Enter the student's name: ")
        self.general_comments = input(f"Please enter your general comments about {self.student_name}: ")
        self.punctuality_engagement = input(f"Please comment on {self.student_name}'s punctuality and engagement, during the course: ")
        self.further_learning = input(f"What are your recommendations for further learning, to aid {self.student_name}: ")
        self.understanding_level = int(input(f"Please rank {self.student_name}'s understanding of the course, from 1-10: "))
        self.contribution_level = int(input(f"Please rank {self.student_name}'s contribution to the course, from 1-10: "))

#This function collates the data that was collected above and merges it into a legible output.
    def generate_feedback(self):
        return f"\n\nFeedback for {self.student_name}:\n\nGeneral Comments about {self.student_name}:\n{self.general_comments}\n\n{self.student_name}'s Punctuality:\n{self.punctuality_engagement}\n\nFurther Learning for {self.student_name}:\n{self.further_learning}\n\nYou ranked {self.student_name} {self.contribution_level} out of 10, for Contribution Level.\n\nYou ranked {self.student_name} {self.understanding_level} out of 10, for Understanding Level\n\n"

#This function saves the feedback a folder named "Feedback" and creates one if it doesn't exist
#It also saves the files as text file, under the name of the student
#A statement is printed, showing where the file has been saved to
    def save_feedback_to_file(self):
        folder_name = "Feedback"
        os.makedirs(folder_name, exist_ok=True)
        file_path = os.path.join(folder_name, f"{self.student_name}_feedback.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.generate_feedback())
        print(f"Feedback saved to {file_path}")

# Creating an instance/variable that allows me to print
Full_Feedback = DevOpsFeedback()
print(Full_Feedback.generate_feedback())

#This instance saves the feedback
Full_Feedback.save_feedback_to_file()
