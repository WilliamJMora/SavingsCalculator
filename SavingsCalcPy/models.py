import math


class Models:

    def __init__(self):

        self.initial_condition = float(input("Current Money in Account:\n$").replace(",", ""))

        self.interest_rate = input("Annual Interest Rate (%):\n").replace("%", "")
        self.interest_rate = float(self.interest_rate) / 100

    def time_to_reach_goal(self):

        goal = float(input("Goal Amount:\n$").replace(",", ""))
        weekly_deposit = float(input("Weekly Contribution:\n$").replace(",", ""))

        a = (weekly_deposit * 52) / self.interest_rate
        constant_of_integration = self.initial_condition + a
        b = (goal + a) / constant_of_integration

        time = round((1 / self.interest_rate) * math.log(b), 2)

        print(f"It will take {time} years to reach your goal.")

    def deposit_needed(self):

        goal = float(input("Goal Amount:\n$").replace(",", ""))
        time = input("Time to Reach Goal: ex. 2, years (use years, months, weeks, or days)):\n").lower().split(" ")

        time_length = float(time[0])
        time_type = time[1]

        if time_type == "year" or "years":
            time_length = time_length
        elif time_type == "month" or "months":
            time_length /= 12
        elif time_type == "week" or "weeks":
            time_length /= 52
        elif time_type == "day" or "days":
            time_length /= 365

        a = (goal - (self.initial_condition * (math.e ** (self.interest_rate * time_length))))
        b = 1300 * (math.e ** (self.interest_rate * time_length) - 1)

        weekly_deposit = round((a / b), 2)

        print(f"You will need to deposit ${weekly_deposit} per week to reach your goal on time.")

    def amount_after_given_time(self):

        time = input("Length of Time for Saving: ex. 2 years (use years, months, weeks, or days): \n").lower().split(" ")
        deposit_frequency = (input("Contribution Frequency (yearly, monthly, weekly, or daily):\n")).lower()
        deposit = float(input(f"How much money will be contributed {deposit_frequency}?\n$").replace(",", ""))

        time_length = int(time[0])
        time_type = time[1]

        if time_type == ("year" or "years"):
            time_length = time_length
        elif time_type == ("month" or "months"):
            time_length /= 12
        elif time_type == ("weeks" or "weeks"):
            time_length /= 52
        elif time_type == ("day" or "days"):
            time_length /= 365

        if deposit_frequency == "yearly":
            deposit = deposit
        elif deposit_frequency == "monthly":
            deposit *= 12
        elif deposit_frequency == "weekly":
            deposit *= 52
        elif deposit_frequency == "daily":
            deposit *= 365

        constant_of_integration = (self.initial_condition * self.interest_rate) + deposit

        a = constant_of_integration * (math.e ** (self.interest_rate * time_length))
        b = a - deposit

        amount = round((b / self.interest_rate), 2)

        print(f"You will have ${amount} in your account after {time[0]} {time[1]}.")