###################################################################################################
#  Topic              : The Binomial Experiment
#
#  Objective          : Simulating the binomial experiment from the subject of probability
#
#  Input              : The program will accept two arguments, where
#                       1st argument = Number of trials (n)
#                       2nd argument = Probability of success (p)
#                       3rd argument = Experiment multiplier
#
#                       For the input to be valid,
#                       (1) 1st argument should be an integer and its value should be at least 3
#                       (2) 2nd argument should be a fraction and its value should be less than 1
#                       (3) 3rd argument should be an integer and its value should be at least 1
#
#  Output             : (1) Probabilities for different values of success (k) using formula for
#                           binomial probability distribution and corresponding graph.
#                       (2) Number of occurrences of different values of success (k) by simulating
#                           coin toss through program and corresponding graph.
###################################################################################################

###################################################################################################
#  Execution sequence :     python3 binomialExperiment.py 1st_argument 2nd_argument 3rd_argument
#  
#  If there is error due to absence of working GUI-backend :    sudo apt-get install python3-tk
#          and un-comment the line after import statements :    matplotlib.use('TkAgg')
#  If there is error due to absence of matplotlib library  :    pip install matplotlib
###################################################################################################

###################################################################################################
#  Sample Input 1     :     python3 binomialExperiment.py 3 1/2 4
#  Sample Output 1    :     --------------------------------------------------------------
#                           PART 1 : Probabilities for different values of success(k)
#                           --------------------------------------------------------------
#                           For k = 0 , P(0) = 1/8
#                           For k = 1 , P(1) = 3/8
#                           For k = 2 , P(2) = 3/8
#                           For k = 3 , P(3) = 1/8
#                           --------------------------------------------------------------
#                           PART 2 : Simulating coin toss through program
#                           --------------------------------------------------------------
#                           For k = 0 , N(0) = 3
#                           For k = 1 , N(1) = 12
#                           For k = 2 , N(2) = 13
#                           For k = 3 , N(3) = 4
#                           --------------------------------------------------------------
#                           PART 3 : Tossing the coin physically
#                           --------------------------------------------------------------
#                           Given, n = 3 , p = 1/2 (three unbiased coins of same type).
#                           Process is repeated 8 times.
#                           Result is attached at the beginning of source file.
#                           --------------------------------------------------------------
#
#  Sample Input 2     :     python3 binomialExperiment.py 4 2/5 3
#  Sample Output 2    :     --------------------------------------------------------------
#                           PART 1 : Probabilities for different values of success(k)
#                           --------------------------------------------------------------
#                           For k = 0 , P(0) = 81/625
#                           For k = 1 , P(1) = 216/625
#                           For k = 2 , P(2) = 216/625
#                           For k = 3 , P(3) = 96/625
#                           For k = 4 , P(4) = 16/625
#                           --------------------------------------------------------------
#                           PART 2 : Simulating coin toss through program
#                           --------------------------------------------------------------
#                           For k = 0 , N(0) = 6
#                           For k = 1 , N(1) = 17
#                           For k = 2 , N(2) = 16
#                           For k = 3 , N(3) = 7
#                           For k = 4 , N(4) = 2
#                           --------------------------------------------------------------
#                           PART 3 : Tossing the coin physically
#                           --------------------------------------------------------------
#                           Given, n = 3 , p = 1/2 (three unbiased coins of same type).
#                           Process is repeated 8 times.
#                           Result is attached at the beginning of source file.
#                           --------------------------------------------------------------
#
#  PART 3 - Result of physical coin toss :
#  Given, n = 3 , p = 1/2 (three unbiased coins of same type) , process is repeated 8 times.
#  (1) Probability of getting 0 heads (TTT)          : P(k=0) = 1/8
#  (2) Probability of getting 1 head  (HTT,THT,TTH)  : P(k=1) = 3/8
#  (3) Probability of getting 2 heads (HHT,HTH,THH)  : P(k=2) = 3/8
#  (4) Probability of getting 3 heads (HHH)          : P(k=3) = 1/8
###################################################################################################

# importing library files
import sys
import math
import random
import array as arr
import fractions
import matplotlib
import matplotlib.pyplot as plt

# setting matplotlib GUI backend to TkAgg
# matplotlib.use('TkAgg')

# defining function to calculate binomial probability
def binomial(n,p,k) :
    probvalue = math.factorial(n)*(p**k)*((1-p)**(n-k))/(math.factorial(k)*math.factorial(n-k))
    prob = fractions.Fraction(probvalue)
    return prob

# defining function to obtain result of a random coin toss
def toss(p) :
    y = random.randint(0,p.denominator-1)
    if y < p.numerator :
        return True
    return False

# defining variable for maximum number of ticks in y-axis to avoid overlapping
MAX_TICKS = 32

# checking number of arguments
num = len(sys.argv)-1
if num != 3 :
    print("Incorrect number of arguments. The program accepts three arguments.")
else :
    validtype = True

    # storing argument values in variables
    try :
        n = int(sys.argv[1])
        p = fractions.Fraction(sys.argv[2])
        em = int(sys.argv[3])
    except ValueError :
        print("Incorrect type of values entered. 1st and 3rd arguments should be integers and 2nd argument should be fraction.")
        validtype = False
    
    # validating entered values
    if validtype :
        if n < 3 :
            print("Value of first argument (number of trials) should be at least 3.")
        elif p >= 1 or p <= 0 :
            print("Value of second argument (probability of success) should be a positive fraction less than 1.")
        elif em < 1 :
            print("Value of third argument (experiment multiplier) should be at least 1.")
        else :
            
            # part 1 : probabilities for different values of success using formula for binomial probability distribution
            print("--------------------------------------------------------------")
            print("PART 1 : Using formula for binomial probability distribution")
            print("--------------------------------------------------------------")
            y_values1 = list(range(0,n+1))
            x_values = list(range(0,n+1))
            for i in range(0,n+1) :
                prob_value = binomial(n,p,i)
                y_values1[i] = prob_value
                print("For k = "+str(i)+" , P("+str(i)+") = "+str(prob_value))
            y_ticks1=list(set(y_values1))
            plt.subplot(1,2,1)
            plt.bar(x_values,y_values1,color='cornflowerblue',zorder=3)
            plt.grid(zorder=0,linestyle='dashed')
            plt.xticks(x_values,x_values)
            plt.yticks(y_ticks1,y_ticks1)
            plt.title("(1) Theoretically")
            plt.xlabel("x = number of heads")
            plt.ylabel("P(x) = probability")

            # part 2 : number of occurrences of different values of success by simulating coin toss through program
            print("--------------------------------------------------------------")
            print("PART 2 : Simulating coin toss through program")
            print("--------------------------------------------------------------")
            outcome = arr.array('i',[0])
            for i in range(0,n) :
                outcome.append(0)
            for i in range(0,(2**n)*em) :
                success = 0
                for j in range(0,n) :
                    if toss(p) == True :
                        success+=1
                outcome[success]+=1
            y_values2 = list(range(0,n+1))
            for i in range(0,n+1) :
                y_values2[i] = outcome[i]
                print("For k = "+str(i)+" , N("+str(i)+") = "+str(outcome[i]))
            maxnum = max(y_values2)
            if maxnum < (2**n)*em :
                maxnum = maxnum + 1
            interval2 = em
            if maxnum / interval2 > MAX_TICKS :
                interval2 = interval2 * int(maxnum/(interval2*MAX_TICKS) + 1)
            y_ticks2 = list(range(0,maxnum+1,interval2))
            if maxnum < y_ticks2[len(y_ticks2)-2] :
                y_ticks2 = y_ticks2[:(len(y_ticks2)-1)]
            if maxnum > y_ticks2[len(y_ticks2)-1] :
                y_ticks2.append(y_ticks2[len(y_ticks2)-1]+interval2)
            plt.subplot(1,2,2)
            plt.bar(x_values,y_values2,color='salmon',zorder=3)
            plt.grid(zorder=0,linestyle='dashed')
            plt.xticks(x_values,x_values)
            plt.yticks(y_ticks2,y_ticks2)
            plt.title("(2) Experimentally")
            plt.xlabel("x = number of heads")
            plt.ylabel("N(x) = number of occurrences")

            # part 3 : probabilities for different values of success by tossing the coin physically
            print("--------------------------------------------------------------")
            print("PART 3 : Tossing the coin physically")
            print("--------------------------------------------------------------")
            print("Given, n = 3 , p = 1/2 (three unbiased coins of same type).")
            print("Process is repeated 8 times.")
            print("Result is attached at the beginning of source file.")
            print("--------------------------------------------------------------")

            # displaying the graphs
            plt.suptitle("The Binomial Experiment ( n = "+str(n)+", p = "+str(p)+", exp. multiplier = "+str(em)+" )")
            plt.subplots_adjust(left=0.115,bottom=0.1,right=0.96,top=0.85,wspace=0.35,hspace=0.4)
            plt.show()