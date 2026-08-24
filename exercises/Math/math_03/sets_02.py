# Survey problem: 100 students: 60 take CS, 40 take Math, 15 take both. 
# How many take neither? Use inclusion-exclusion. 
# Verify with Python sets.

student_cs = 60
student_math = 40
student_both = 15

union_count = abs(student_cs) + abs(student_math) - abs(student_both)
neither_count = 100 - union_count

print(neither_count)

# Universe of 100 students (IDs 1 to 100)
all_students = set(range(1, 101))

# 1. CS Students (60 total)
# Includes IDs 1-15 (Both) and 16-60 (CS Only)
cs_students = set(range(1, 61))

# 2. Math Students (40 total)
# Includes IDs 1-15 (Both) and 61-85 (Math Only)
# Note: We skip 16-60 to avoid extra overlap
math_students = set(range(1, 16)) | set(range(61, 86))

# All students that take something
all_enrolled = abs(len(cs_students)) + abs(len(math_students) - abs(len(cs_students & math_students)))

# 3. Neither (15 total)
# Students not in CS and not in Math (IDs 86-100)
neither_students = all_students - (cs_students | math_students)

# Verification
print(f"CS Count: {len(cs_students)}")           # 60
print(f"Math Count: {len(math_students)}")       # 40
print(f"Both Count: {len(cs_students & math_students)}") # 15
print(f"Neither Count: {len(neither_students)}") # 15
print(f"Neither IDs: {sorted(neither_students)}")
print(f"All students that take something: {all_enrolled}") 
# Output: [86, 87, ..., 100]   