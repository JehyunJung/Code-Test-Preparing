import fibonacci_dp, fibonacci_recursion
import sys,time

functions=[fibonacci_dp.fibo,fibonacci_recursion.fibo]
n=int(sys.argv[1])
for function in functions:
  start=time.time()
  function(n)
  print(function.__module__)
  print("Execution Time: "+str((time.time()-start))+"s")
