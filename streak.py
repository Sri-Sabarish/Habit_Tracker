from datetime import datetime,timedelta
# first we are converting the list of tuples data from logs to dictionary type for easy searching
def logs_to_dict(logs):
    log_dict={} # initializing empty dictionary
    for date_str,status in logs:
        log_dict[date_str]=status
    return log_dict

#next we are calculating Streaks for completed tasks
def calculate_current_streak(logs):
    log_dict=logs_to_dict(logs)
    streak=0
    current_date=datetime.today().date()  #getting today's date
    while True:
        date_str=current_date.strftime("%Y-%m-%d")  #for proper yy mm dd format
        if log_dict.get(date_str)=="done":  #checking today's status
            streak+=1
            current_date-=timedelta(days=1) #moving one day back to check that day's status
        else:
            break
    return streak  
#calculate best streak - longest number of days an activity performed repeatedly
def calculate_best_streak(logs):
    log_dict=logs_to_dict(logs)
    if not log_dict:
        return 0
    all_dates=sorted(log_dict.keys()) #sort dates
    #initializing
    best=0
    current=0
    prev_date=None
    for date_str in all_dates:
        date_obj=datetime.strptime(date_str,"%Y-%m-%d").date()
        status=log_dict[date_str]
        if status=="done":
            if prev_date is not None and (date_obj-prev_date).days==1:
                current+=1
            else:
                current=1
            best=max(best,current)
        else:
            current=0
        prev_date=date_obj
    return best  
#calculate consistency percentage
def calculate_consistency(logs):
    if not logs:
        return 0
    done_count=0
    for date,status in logs:
        if status=="done":
            done_count+=1
    total_count=len(logs) 
    consistency=(done_count/total_count)*100
    return round(consistency,1)   
if __name__ == "__main__":
    fake_logs = [
        ("2026-07-12", "done"),
        ("2026-07-13", "done"),
        ("2026-07-14", "missed"),
        ("2026-07-15", "done"),
    ]
    print("Best streak:", calculate_best_streak(fake_logs))
    print("Consistency:", calculate_consistency(fake_logs))
           