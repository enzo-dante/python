num_ki = input('How many kilometers did you run today?\n')

ki_to_mi_ratio = 0.621371

num_mi = float(int(num_ki) * ki_to_mi_ratio)
num_mi = round(num_mi, 2)

# to avoid compilation issue, just use f-strings instead of concatenation
print(f'Your {num_ki}km run was {num_mi}mi')

