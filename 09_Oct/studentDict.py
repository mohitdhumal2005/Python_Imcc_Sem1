# Create Dictionary with Student Details:
students = {
    101 : {"Name":"Rohit", "Scores":[20,20,25]},
    102 : {"Name":"Virat", "Scores":[45,60,50]},
    103 : {"Name":"Karan", "Scores":[55,12,43]},
    104 : {"Name":"Priya", "Scores":[0,14,95]},
    105 : {"Name":"Sneha", "Scores":[49,51,47,33]}
}
# Calculate the average score and flag pass/fail

for sid, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 30   #Boolean Flag
    
# Print names of Students who Passed:
print("Students Who Passes: ")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"]," - ", details["Scores"]," - ",details["Average"])
        # print(details["Scores"])