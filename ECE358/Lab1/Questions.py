import HelperFunctions
import statistics
import SimulatorMM1
import SimulatorMM1K

def question_1():
    print("Question 1")

    random_variables = []

    for i in range(0,1000):
       random_variables.append(HelperFunctions.generate_exponential_random_numbers(75))

    mean = statistics.mean(random_variables)
    variance = statistics.variance(random_variables)

    print("Generated Mean: ", mean)
    print("Generated Variance: ", variance) 
    print("-----------------------------------------------")


def question_3():
    print("Question 3")
    L = 2000
    C = 1000000
    T = 1000
    rho = [0.35, 0.45, 0.55, 0.65, 0.75, 0.85]
    
    for rho_value in rho:
        print("FOR RHO = ", rho_value)
        lam = HelperFunctions.lambda_value(rho_value, L, C)
        alpha = HelperFunctions.alpha_value(rho_value, L, C)

        SimulatorMM1.observer(T, alpha)
        SimulatorMM1.arrival(T, lam, L)
        SimulatorMM1.departure(C)
        SimulatorMM1.sort()
        SimulatorMM1.dequeue()

    print("-----------------------------------------------")

def question_4():
    print("Question 4")
    L = 2000
    C = 1000000
    T = 1000
    
    rho_value = 1.2
    
    print("FOR RHO = ", rho_value)
    lam = HelperFunctions.lambda_value(rho_value, L, C)
    alpha = HelperFunctions.alpha_value(rho_value, L, C)

    SimulatorMM1.observer(T, alpha)
    SimulatorMM1.arrival(T, lam, L)
    SimulatorMM1.departure(C)
    SimulatorMM1.sort()
    SimulatorMM1.dequeue()

    print("-----------------------------------------------")

def question_6():
    print("Question 6")
    L = 2000
    C = 1000000
    T = 1000
    rho = [0.60, 0.70, 0.80, 0.90, 1.0, 1.1, 1.2, 1.3, 1.4]
    K = [10, 25, 50]

    for k_value in K:
        print("FOR K = ",   k_value)
        for rho_value in rho:
            print("FOR RHO = ", rho_value)
            lam = HelperFunctions.lambda_value(rho_value, L, C)
            alpha = HelperFunctions.alpha_value(rho_value, L, C)

            SimulatorMM1K.observer(T, alpha)
            SimulatorMM1K.arrival(T, lam, L)
            SimulatorMM1K.departure(C)
            SimulatorMM1K.sort()
            SimulatorMM1K.dequeue(k_value)

    print("-----------------------------------------------")

def main():
    #question_1()
   # question_3()
   # question_4()
   question_6()

main()