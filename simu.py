# JACOBIAN DETERMINANT PROGRAM
import sympy as sp
# Score
score = 0

# Number of variables/functions
n = int(input("Enter number of variables/functions: "))

# Variable names
var_names = input(f"Enter {n} variables separated by space: ").split()

# Checking count
if len(var_names) != n:
    print("Variable count mismatch!")
    exit()

# Creating symbolic variables
variables = sp.symbols(var_names)

# Rules
print("\nRULES")
print("Correct derivative = +5 points")
print("Correct matrix row = +10 points")
print("Wrong attempt = -1 point")
print("Hint used = -2 points\n")

# Taking functions
functions = []

for i in range(n):
    func = input(f"Enter function f{i+1}: ")
    functions.append(sp.sympify(func))

print("\n=== FUNCTIONS ===")

for i in range(n):
    print(f"f{i+1} =", functions[i])

# Finding derivatives and forming Jacobian matrix
jacobian_matrix = []

print("\n=== PARTIAL DERIVATIVES ===")

for i in range(n):

    row = []

    for j in range(n):

        derivative = sp.diff(functions[i], variables[j])

        print(f"\nFind ∂f{i+1}/∂{variables[j]}")

        chances = 3

        while chances > 0:

            user_answer = input("Your answer: ")

            user_derivative = sp.sympify(user_answer)

            if sp.simplify(user_derivative - derivative) == 0:

                print("Correct!")
                score += 5

                print("Score =", score)

                break

            else:

                chances -= 1
                score -= 1

                print("Wrong answer.")
                print("Score =", score)

                if chances > 0:

                    print("Please try again.")
                    print("Remaining chances:", chances)

                else:

                    print("Hint:", derivative)

                    score -= 2

                    print("Hint penalty applied.")
                    print("Score =", score)

        print(f"∂f{i+1}/∂{variables[j]} = {derivative}")

        row.append(derivative)

    jacobian_matrix.append(row)

# Converting into matrix
J = sp.Matrix(jacobian_matrix)

# ---------------- MATRIX SIMULATION ----------------

print("\n=== ENTER JACOBIAN MATRIX ROW BY ROW ===")

for i in range(n):

    chances = 3

    while chances > 0:

        user_row = input(
            f"Enter row {i+1} elements separated by space: "
        ).split()

        # Convert into sympy expressions
        user_row = [sp.sympify(x) for x in user_row]

        correct_row = jacobian_matrix[i]

        # Checking row
        correct = True

        if len(user_row) != n:
            correct = False

        else:

            for j in range(n):

                if sp.simplify(user_row[j] - correct_row[j]) != 0:
                    correct = False
                    break

        if correct:

            print("Correct row!")
            score += 10

            print("Score =", score)

            break

        else:

            chances -= 1
            score -= 1

            print("Wrong row.")
            print("Score =", score)

            if chances > 0:

                print("Please try again.")
                print("Remaining chances:", chances)

            else:

                print("Hint:", correct_row)

                score -= 2

                print("Hint penalty applied.")
                print("Score =", score)

# ---------------------------------------------------

print("\n=== JACOBIAN MATRIX ===")
sp.pprint(J)

# Determinant
determinant = J.det()

print("\n=== DETERMINANT BEFORE SIMPLIFYING ===")
print(determinant)

# Simplifying
simplified_det = sp.simplify(determinant)

print("\n=== SIMPLIFIED JACOBIAN ===")
print(simplified_det)

# ---------------- VALUE SUBSTITUTION ----------------

choice = input("\nDo you want to substitute values? (yes/no): ")

if choice.lower() == "yes":

    values = {}

    print("\nEnter values for variables:")

    for var in variables:

        val = float(input(f"{var} = "))

        values[var] = val

    # Substitute values in Jacobian matrix
    substituted_matrix = J.subs(values)

    print("\n=== JACOBIAN MATRIX AFTER SUBSTITUTION ===")

    sp.pprint(substituted_matrix)

    # Determinant after substitution
    substituted_det = substituted_matrix.det()

    print("\n=== DETERMINANT AFTER SUBSTITUTION ===")
    print(substituted_det)

    score += 10

    print("\nBonus +10 points")
    print("Score =", score)

# ---------------- FINAL SCORE ----------------

print("\n=== FINAL SCORE ===")
print("Your Score =", score)

if score >= 80:
    print("Outstanding Performance!")

elif score >= 50:
    print("Excellent Work!")

elif score >= 25:
    print("Good Attempt!")

else:
    print("Keep Practicing!")
