import math
from re import U


class ApproximateIntegrations:


    def __init__(self, expression, args, lowerBound, topBound, interval, accuracyRange):
        self.exp = expression
        self.fx = args
        self.x = []
        self.lower = lowerBound
        self.top = topBound
        self.range = interval
        self.accuracy_range = accuracyRange
        self.abs_value_second_derivative = 14 # calculate derivative
        self.abs_value_fourth_derivative = 14 # Calculate derivative 
        self.trapezoidal_enum()
        self.midpoint_enum()
        self.simpsons_enum()
        self.trapezoidal_approximation()
        self.midpoint_approximation()
        self.simpsons_approximation()
        self.trapezoidal_error()
        self.midpoint_error()
        self.simpsons_error()
        self.actual_error_t = 28 - self.T # calculate Absolute value of the integral (28)
        self.actual_error_m = 28 - self.M
        self.actual_error_s = 28 - self.S
        self.trapezoidal_error_accuracy()
        self.midpoint_error_accuracy()
        self.simpsons_error_accuracy()
    
    def __str__(self) -> str:
        return(f"f(x) = {self.exp}\nIntegral {self.lower}->{self.range}\nT = {self.T}\t| error = {self.t_error:.6f}\t| |E| < {self.actual_error_t:.6f}\t| N = {self.t_accuracy_error:.0f}\nM = {self.M}\t| error = {self.m_error:.6f}\t| |E| < {self.actual_error_m:.6f}\t| N = {self.m_accuracy_error:.0f}\nS = {self.S}\t| error = {self.s_error:.6f}\t| |E| < {self.actual_error_s:.6f}\t| N = {self.s_accuracy_error:.0f}")

    
    def trapezoidal_approximation(self):    
        self.T = (self.top/self.range)*(1/2)*(2*(self.t_enum))
        # return(T)

    
    def midpoint_approximation(self):
        self.M = (self.top/self.range)*self.m_enum

    
    def simpsons_approximation(self):
        self.S = (self.top/self.range)*(1/3)*self.s_enum
        # return(S)

    def trapezoidal_enum(self):
        self.t_enum=0
        self.x = []
        for i in range(1, self.range+1):
            self.x.append((i*pi)/self.range)
        for i in range(len(self.x)):
            self.x[i] = f(self.x[i])
            self.t_enum += self.x[i]
        


    def midpoint_enum(self):
        self.m_enum = 0
        self.x = []
        for i in range(1, 2*self.range, 2):
            self.x.append((i*pi)/(2*self.range))
            # print(f"{i}𝜋/20 = {x[-1]}")
        for i in range(len(self.x)):
            self.x[i] = f(self.x[i])
            # print(f"14sin({i}𝜋/20) = {x[i]}")
            self.m_enum += self.x[i]


    
    def simpsons_enum(self):
        self.s_enum = 0
        self.x=[]
        for i in range(self.range):
            if (i%2==0):
               self.x.append(2*f((i*pi)/self.range))
            else:
                self.x.append(4*f((i*pi)/self.range))
            # x[i] = f(x[i])
            self.s_enum += self.x[i]


    
    def trapezoidal_error(self):
        self.t_error = (self.abs_value_second_derivative)*(pi**3)/(12*(self.range**2))
    
    def midpoint_error(self):
        self.m_error = self.abs_value_second_derivative*(pi**3)/(24*(self.range**2))

    def simpsons_error(self):
        self.s_error = self.abs_value_fourth_derivative*(pi**5)/(180*(self.range**4))

    def trapezoidal_error_accuracy(self):
        self.t_accuracy_error = int(
            math.sqrt((self.abs_value_second_derivative*(self.range**self.accuracy_range)*pi**3)/(12)))+1

    def midpoint_error_accuracy(self):
        self.m_accuracy_error = int(
            math.sqrt((self.abs_value_second_derivative*(self.range**self.accuracy_range)*pi**3)/(24)))+1

    def simpsons_error_accuracy(self):
        self.s_accuracy_error = int((self.abs_value_fourth_derivative*(
            self.range**self.accuracy_range*pi**5)/(180))**(1/4))
        if(self.s_accuracy_error % 2 != 0):
            self.s_accuracy_error += 1
        else:
            self.s_accuracy_error += 2


    # @staticmethod
    # def trapezoidal_approximation(subintervalEnum, topBound, interval):    
    #     T = (topBound/interval)*(1/2)*(2*(subintervalEnum))
    #     return(T)
    # @staticmethod
    # def midpoint_approximation(midpointEnum, topBound, interval):
    #     M = (topBound/interval)*midpointEnum
    #     return(M)
    # @staticmethod
    # def simpsons_approximation(simpsonsEnum, topBound, interval):
    #     S = (topBound/interval)*(1/3)*simpsonsEnum
    #     return(S)
    # @staticmethod
    # def trapezoidal_enum(x, interval):
    #     TE=0
    #     for i in range(1, interval+1):
    #         x.append((i*pi)/interval)
    #         # print(f"{i}𝜋/20 = {x[i]}")
    #     for i in range(len(x)):
    #         x[i] = f(x[i])
    #         # print(f"\t14sin({i}𝜋/10) = {x[i]}")
    #         TE += x[i]
    #     return (TE)
    # @staticmethod
    # def midpoint_enum(x, interval):
    #     ME = 0
    #     x=[]
    #     for i in range(1, 2*interval, 2):
    #         x.append((i*pi)/(2*interval))
    #         # print(f"{i}𝜋/20 = {x[-1]}")
    #     for i in range(len(x)):
    #         x[i] = f(x[i])
    #         # print(f"14sin({i}𝜋/20) = {x[i]}")
    #         ME += x[i]
    #     return(ME)
    # @staticmethod
    # def simpsons_enum(x, interval):
    #     SE = 0
    #     x=[]
    #     for i in range(interval):
    #         if (i%2==0):
    #            x.append(2*f((i*pi)/interval))
    #         else:
    #             x.append(4*f((i*pi)/interval))
    #         # x[i] = f(x[i])
    #         SE += x[i]
    #     return(SE)
    # @staticmethod
    # def trapezoidal_error(abs_value_second_derivative, interval):
    #     error = (abs_value_second_derivative)*(pi**3)/(12*(interval**2))
    #     return (error)
    # @staticmethod
    # def simpsons_error(abs_value_fourth_derivative, interval):
    #     error = abs_value_fourth_derivative*(pi**5)/(180*(interval**4))
    #     return (error)
    # @staticmethod
    # def trapezoidal_error_accuracy(abs_value_second_derivative, interval, accuracyRange):
    #     error = int(
    #         math.sqrt((abs_value_second_derivative*(interval**accuracyRange)*pi**3)/(12)))
    #     return (error+1)
    # @staticmethod
    # def midpoint_error_accuracy(abs_value_second_derivative, interval, accuracyRange):
    #     error = int(
    #         math.sqrt((abs_value_second_derivative*(interval**accuracyRange)*pi**3)/(24)))
    #     return (error+1)
    # @staticmethod
    # def simpsons_error_accuracy(abs_value_fourth_derivative, interval, accuracyRange):
    #     error = int((abs_value_fourth_derivative*(
    #         interval**accuracyRange*pi**5)/(180))**(1/4))
    #     if(error%2!=0):
    #         error+=1
    #     else:
    #         error+=2
    #     return (error)


class Integration:
    def __init__(self) -> None:
        #
        pass

    @staticmethod
    def integrate(N, a, b):
        #
        u = 0
        e = 0
        for n in range(1, N+1):
            u += f(a+((n-(1/2))*((b-a)/N)))
        e = ((b-a)/N)*u
        return(e)

    def anti_derivative(self):
        #
        pass


pi = math.pi

def f(u):
    y = 14*math.sin(u)
    return(y)

# interval=10
# topBound = pi
# lowerBound = 0
# accuracyRange = 5
# anti = int(Integration.integrate(10, lowerBound, topBound)) #Doesn't work
# second_derivative = 0
# fourth_derivative = 0


# x = []
# tEnum = ApproximateIntegrations.trapezoidal_enum(x, interval)
# T = ApproximateIntegrations.trapezoidal_approximation(tEnum, topBound, interval)
# errorT = anti-T 
# actualErrorT = ApproximateIntegrations.trapezoidal_error(14, interval)
# accuracyError = ApproximateIntegrations.trapezoidal_error_accuracy(14, interval, accuracyRange)
# print(f"T = {T:.6f}\t| error = {errorT:.6f}\t| |E| < {actualErrorT:.6f}\t| N = {accuracyError:.0f}")

# x = []
# midpointEnum = ApproximateIntegrations.midpoint_enum(x, interval)
# M = ApproximateIntegrations.midpoint_approximation(midpointEnum, topBound, interval)
# errorM = anti-M 
# actualErrorM = ApproximateIntegrations.midpoint_error(14, interval)
# accuracyError = ApproximateIntegrations.midpoint_error_accuracy(14, interval, accuracyRange)
# print(f"M = {M:.6f}\t| error = {errorM:.6f}\t| |E| < {actualErrorM:.6f}\t| N = {accuracyError:.0f}")

# x = []
# simpsonsEnum = ApproximateIntegrations.simpsons_enum(x, interval)
# S = ApproximateIntegrations.simpsons_approximation(simpsonsEnum, topBound, interval)
# errorS = anti-S 
# actualErrorS = ApproximateIntegrations.simpsons_error(14, interval)
# accuracyError = ApproximateIntegrations.simpsons_error_accuracy(14, interval, accuracyRange)
# print(f"S = {S:.6f}\t| error = {errorS:.6f}\t| |E| < {actualErrorS:.6f}\t| N = {accuracyError:.0f}")

def ooo(x): return (8/x)

obj = ApproximateIntegrations("8/x dx", ooo, 1, 6, 100, 5)
print(obj)
