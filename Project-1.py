def solve_circuit(b, c):
  q = (b and c) or (b and not c)
  return q

print("B | C | Q")
print("---------")

#Testing all possible input combinations
# B=0, C=0
q_00 = solve_circuit(0, 0)
print(f"0 | 0 | {int(q_00)}")

# B=0, C=1
q_01 = solve_circuit(0, 1)
print(f"0 | 1 | {int(q_01)}")

# B=1, C=0
q_10 = solve_circuit(1, 0)
print(f"1 | 0 | {int(q_10)}")

# B=1, C=1
q_11 = solve_circuit(1, 1)
print(f"1 | 1 | {int(q_11)}")

