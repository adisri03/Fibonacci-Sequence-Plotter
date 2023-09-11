import matplotlib.pyplot as plt
import plotly.graph_objects as go

def fibo(n):
    if n>=0: 
       index = range(n+1)
       x = [0,1]
       for k in index[2:]:
           x.append(x[k-1] + x[k-2])
       return x[n]
    else:
       n=-(n-1)
       index = range(n+1)
       x = [1,0]
       for k in index[2:]:
           x.append(x[k-2] - x[k-1])
       x.reverse()
    return x[0]


fib_arr=[]
a = 
b = 
for i in range(a,b):
   fib_arr.append(fibo(i))


# Plot the Fibonacci numbers
plt.plot(fib_arr)

# Set the title of the plot
plt.title("Fibonacci Sequence")

# Set the x-axis label
plt.xlabel("Index")

# Set the y-axis label
plt.ylabel("Number")

# Show the plot
plt.show()
