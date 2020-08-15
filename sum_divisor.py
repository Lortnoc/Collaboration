def sum_divisors(n):
  summ = 0
  q = 0
  while q < n:
      if n == 0:
          return 0
      elif n % q == 0:
          summ =summ +q
      else:
          q = q + 1
    
     
  # Return the sum of all divisors of n, not including n
  return summ

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

"""
def sum_divisors(n):
  sum = 1 
  div = 2
  if n == 0:
    return 0

  while div < n/2+1:
        if n % div == 0:
          sum =sum +div
        div+=1  
    
     
  # Return the sum of all divisors of n, not including n
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
"""