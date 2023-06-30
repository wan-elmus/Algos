
from itertools import combinations

def hire_counselors(n, m, qualifications, k):
    for comb in combinations(range(m), k):
        sports_covered = set(range(n))
        for applicant in comb:
            sports_covered &= set(i for i, qualified in enumerate(qualifications[applicant]) if qualified)
            if not sports_covered:
                break
        if sports_covered:
            return True
    return False

# Example usage
n = 3
m = 5
qualifications = [
    [True, False, True],  # Applicant 0 is qualified for baseball and basketball
    [False, True, False], # Applicant 1 is qualified for volleyball
    [True, True, True],   # Applicant 2 is qualified for all sports
    [False, True, True],  # Applicant 3 is qualified for volleyball and basketball
    [True, True, False]   # Applicant 4 is qualified for baseball and volleyball
]
k = 3

result = hire_counselors(n, m, qualifications, k)
print(result)
