from math import log10, sqrt

def equation(f, k, Re, R):
    return 1 / sqrt(f) - 2.0 * log10(R/k) - 1.74 + 2 * log10(1 + 18.7 * R / (k * Re * sqrt(f)))

# Iterative method
# def find_f(k, Re, R, start=0.00001, end=0.99999, step=0.00001):
#     best_f = None
#     min_error = float('inf')

#     current_f = start
#     while current_f <= end:
#         current_error = abs(equation(current_f, k, Re, R))
        
#         if current_error < min_error:
#             min_error = current_error
#             best_f = current_f

#         current_f += step

#     return best_f

# Newton-Raphson method
def derivative_equation(f, k, Re, R):
    return (-9.35 - 8.12131 * sqrt(f)) * R - 0.5 *sqrt(f) * k * Re / (18.7 * f**(3/2) * R + f**2 * k * Re)

def newton(k, Re, R, max_iter=100000, tol=1e-6):
    f = 0.02
    for i in range(max_iter):
        f = f -  equation(f, k, Re, R)/derivative_equation(f, k, Re, R)
        if abs(equation(f, k, Re, R)) < tol:
            break
    return f

def problem_1():
    l = float(input("Enter the length of pipe: "))
    k = float(input("Enter the average height of roughness: "))
    Q = float(input("Enter the discharge: "))
    D = float(input("Enter the diameter of pipe: "))
    nu = float(input("Enter the kinematic viscosity: "))
    # l = 400
    # k = 0.00025
    # Q = 0.15
    # D = 0.2
    # nu = 0.00001
    v = Q / (3.14159265 * D ** 2 / 4)
    Re = v * D / nu
    f = newton(k, Re, D/2)
    x = l*v**2/(19.62*D)
    hf = f * x
    print("The head loss is: ", round(hf, 3))

def problem_2():
    # l = float(input("Enter the length of pipe: "))
    # k = float(input("Enter the average height of roughness: "))
    # hf = float(input("Enter the head loss: "))
    # D = float(input("Enter the diameter of pipe: "))
    # nu = float(input("Enter the kinematic viscosity: "))
    l = 400
    k = 0.00025
    D = 0.2
    nu = 0.00001
    hf = 53.6260619067951
    f = 0.02
    for i in range(10):
        x = 12.1 * hf * D**5 / l
        Q = sqrt(x/f)
        v = Q / (3.14159265 * D ** 2 / 4)
        Re = v * D / nu
        f = newton(k, Re, D/2)
        Q = sqrt(x/f)
    print("The discharge is: ", round(Q, 3))

def problem_3():
    # l = float(input("Enter the length of pipe: "))
    # k = float(input("Enter the average height of roughness: "))
    # hf = float(input("Enter the head loss: "))
    # Q = float(input("Enter the discharge: "))
    # nu = float(input("Enter the kinematic viscosity: "))
    l = 400
    k = 0.00025
    Q = 0.15
    nu = 0.00001
    hf = 53.6260619067951
    f = 0.02
    for i in range(10):
        x = l * Q**2 / (12.1 * hf)
        D = f**(1/3) * x
        v = Q / (3.14159265 * D ** 2 / 4)
        Re = v * D / nu
        f = newton(k, Re, D/2) 
        D = f**(1/3) * x
    print("Diameter of pipe: ", round(D, 3))


def main():
    scanf = int(input("Enter the problem number: "))
    if scanf == 1:
        problem_1()
    elif scanf == 2:
        problem_2()
    elif scanf == 3:
        problem_3()

if __name__ == "__main__":
    main()
