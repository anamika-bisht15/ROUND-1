<img width="1024" height="1024" alt="Gemini_Generated_Image_q62s0q62s0q62s0q" src="https://github.com/user-attachments/assets/0c15ef9f-f9d3-46c8-a39e-97ceb211c97d" />
## Workflow Breakdown

Complaint Submission: The process begins when a user submits a complaint in text format.
Text Processing: The raw text undergoes "Cleaning and Tokenization" to prepare it for analysis.
NLP Analysis: The processed text is fed into an NLP Model, which performs three key concurrent tasks:
Complaint Category Classification: Identifying the department involved, such as Water, Electricity, Roads, or Police.
Sentiment and Urgency Analysis: Determining the emotional tone and how critical the issue is.
Priority Assignment: Based on the analysis, the system labels the grievance as High, Medium, or Low priority.
Storage: The analyzed complaint and its assigned priority are stored in a database.
User Feedback: Finally, a Chatbot retrieves the information to provide a real-time complaint status update to the user.
