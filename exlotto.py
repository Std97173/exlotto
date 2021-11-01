import random

class exlotto:
  def lotto():
  	lotto=random.sample(range(1,48),6)
  	lotto.sort()
  	return lotto