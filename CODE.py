import json

jobs = {"Python Developer": 1}   # job name -> vacancies
candidates = {}                  # candidate name -> {job: status}
interviews = []                  # booked (date, time) slots

def apply_job(name, job):
    if job not in jobs:
        print("Job not found")
        return
    if name not in candidates:
        candidates[name] = {}
    candidates[name][job] = "Applied"

def schedule(name, job, date, time):
    if (date, time) in interviews:
        print("Slot already booked")
        return
    interviews.append((date, time))
    candidates[name][job] = "Interview"

def update(name, job, status):
    if status == "Selected":
        if jobs[job] == 0:
            print("No vacancies left")
            return
        jobs[job] = jobs[job] - 1
    candidates[name][job] = status

def report():
    statuses = []
    for name in candidates:
        statuses += list(candidates[name].values())
    print("Total applications:", len(statuses))
    print("Selected:", statuses.count("Selected"))
    print("Selection rate:", statuses.count("Selected") / len(statuses) * 100, "%")

apply_job("Asha", "Python Developer")
apply_job("Ravi", "Python Developer")
schedule("Asha", "Python Developer", "20-10-2026", "10:00")
schedule("Ravi", "Python Developer", "20-10-2026", "10:00")   # same slot
update("Asha", "Python Developer", "Selected")
report()
json.dump({"jobs": jobs, "candidates": candidates}, open("hr_data.json", "w"))
