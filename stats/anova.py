from functools import reduce


#group1 = [1, 2, 5]
group1 = [10, 20, 50, 40, 30]
group2 = [2, 4, 2, 3, 2.5]
group3 = [2, 3, 4, 3.5, 4]

data = [group1, group2, group3]

#
# Step 1 - Hypothesis
#
#  H0: m1 = m2 = m3
#  Ha: at least one differnce among the means
#  a = 0.05


#
# Step 2 Analyze degrees of freedom
#
points_per_group = [len(grp) for grp in data]
total_points = sum(points_per_group)

k = len(data)       # Number of groups
N = total_points    # Number of data points

# Calculate Degrees of Freedom (F-Distribution)
df_between = k - 1
df_within = N - k
df_total = df_between + df_within
F_crit = 5.14   # From table of F(2,6)

print(f"DF_Between={df_between} DF_Within={df_within}")


#
# Step 3 Sum of squares
#
# a. mean for each condition
mean_x = [sum(group) / len(group) for group in data]
for idx in range(len(data)):
    print(f"mean_x{idx}={mean_x[idx]:.2f}")

# b. grand mean
sum_x = [sum(group) for group in data]
G = sum(sum_x)
grand_mean = G / N      # X_bar
print(f"Grand mean={grand_mean:.2f}")

# c. Sum of squares total
# ss_total = sum[(x - X_bar)^2]
def sum_squares(S, x):
    return S + (x-grand_mean) ** 2

all_data_points = reduce(lambda S,x: S+x, data)
SS_total = reduce(sum_squares, all_data_points, 0)
print(f"SumSquare_Total={SS_total:.2f}")

# d. Sum of squares within
SS_within = 0
for idx in range(len(data)):
    grp_mean = mean_x[idx]
    grp = data[idx]
    SS_within = reduce(lambda S,x: S + (x-grp_mean) ** 2, grp, SS_within)
print(f"SumSquare_within={SS_within:.2f}")

# e. Sum of squares between
SS_between = SS_total - SS_within
print(f"SumSquare_between={SS_between:.2f}")



#
# STEP 4 Mean squares
#
MS_between = SS_between / df_between
MS_within = SS_within / df_within
print(f"MeanSquare between={MS_between:.2f}  MeanSquare within={MS_within:.2f}")

#
# STEP 5 Calculate F
#
# F = Variance between / Variance within
F = MS_between / MS_within
print(f"F={F:.2f}")

if F < F_crit:
    print("F is not in critical region, cannot reject H0")
else:
    print("F is within the critical region, reject H0 and accept H1")
