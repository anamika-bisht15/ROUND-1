print("AI-Based Grievance Redressal System Prototype")

complaint = input("Enter your complaint: ").lower()

if "water" in complaint:
    category = "Water"
    priority = "High"
elif "electricity" in complaint:
    category = "Electricity"
    priority = "Medium"
elif "road" in complaint:
    category = "Roads"
    priority = "Medium"
elif "police" in complaint:
    category = "Police"
    priority = "High"
else:
    category = "General"
    priority = "Low"

print("\nComplaint Analysis Result:")
print("Category:", category)
print("Priority:", priority)
print("Status: Submitted Successfully")
