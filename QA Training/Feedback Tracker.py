# An app that will help automate the writing of student feedback adhering to 
    #formatting requirements. 

    #reqs:
        #- The feedback must be written to a .txt file with the file name 
         #   including the students name. 
        #- The text in the file must have the headers 'General comments', 
         #   'Punctuality and engagement' and 'further learning'. Each header will have
          #  a short paragraph of text.
        #- All files to be written to a sub-folder named "feedback_files"
        #- The file should open automatically in a text editor for manual review.
        #- The user of the app should input students names.
        #- Inputs for marks/grades students recieve for specific factors such    
        #    as 'understanding_level', 'contribution_level' etc. 
        #- The marks should be used to format believable sentances to be written 
        #    to the file.
        #- The feedback is expected to have correct grammar and appear to be 
        #    written personally.


#example final format:

#General comments
#Lyudmil worked hard in this module, completing all his labs to a good standard. 
#He picked up DevOps tooling quickly, demonstrating a good level of existing knowledge. 
#He contributed to class discussions and worked well independently.  

#Learner Punctuality and engagement 
#Lyudmil was always punctual throughout the module and engaged well. 

#Recommendations on further learning
#Continue to practice and explore good pipeline design and integrate docker and 
#monitoring into your projects. 

#Feedback will be given on Bud - (written by me manually!) Im looking for good and 
#extensible design, with comments/doc strings explaining decisions. 
#Deadline: end of module - must be emailed (in body of email not attatchment).
#spend 1 - 2 hours max! 

import os

class DevOpsFeedback:
    def __init__(self, studentname, puncutality_engagement, future_learning, general_comments):
        self.studentname = studentname
        self.punctulality_engagement = puncutality_engagement
        self.future_learning = future_learning
        self.general_comments = general_comments 
        self.feedback_folder = "feedback_files"
        self.feedback_content = ""

    def generate_feedback(self):
        general_comments = f"General comments: {self.generate.general_comments()}\n"
        punctuality_engagement = f"Punctuality and engagement: {self.generate.punctuality_engagement()}\n"
        further_learning = f"Recommendations for further learning: {self.generate.further_learning()}\n"
        self.feedback_content = f"{general_comments}\n{punctuality_engagement}\n{further_learning}"

    def generate_general_comments(self):
        input f"Please enter your general feedback for {studentname}: "

    def generate_punctuality_engagement(self):
        pande = input f"Was {studentname} punctual and engaged? Please answer with 'Yes'or 'No'"
        if pande == Yes
