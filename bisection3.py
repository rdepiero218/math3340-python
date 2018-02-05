
# written with python 3--print commands must be changed
def bisection(f, a, b, maxIters, TOL, printer=False):

#verifying the STEP1, a and b with different signs
    if f(a)*f(b)>0:
        print("Error, f(a) and f(b) should have opposite signs")
        return False
    #Assigning the current extreme values, STEP2
    xL = a
    xR = b
    #Iterations
    n = 1
    while n<=maxIters:
        #Bisection, STEP3
        xM = (xL+xR)/2.0
        #Evaluating function in pi, STEP4 and STEP5
        if printer:
            print("Value for %d iterations:"%(n),xM)
        #Condition A
        if f(xM)*f(xL)<0:
            xR = xM
        #Condition B
        else:
            xL = xM
        #Condition C: repeat the cycle
        if abs(f(xM)) < TOL:
        	break

        if n == maxIters:
        	print('Maximum number of iterations reached')

        n+=1
    #Final result
    return xM