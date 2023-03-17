import datetime

user_input=input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

dateline_date = (datetime.datetime.strptime(deadline, "%d.%m.%Y"))
today_date = datetime.datetime.today()
time_till = dateline_date - today_date

hours_till = int(time_till.total_seconds()/60/60)
#calcula cuantos dias para la meta

print(f"Dear user! Time remaining for your goal :{goal} is {hours_till} hours.")
print(f"Dear user! Time remaining for your goal :{goal} is {time_till.days} days.")

