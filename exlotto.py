def lotto(a,n,m):
  import random
  lotto=random.sample(range(a,n+1),m)
  lotto.sort()
  return lotto
