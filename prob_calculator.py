import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**arguments):
    self.contents=[]
    for key,value in arguments.items():
      for i in range(0,value):
        self.contents.append(key)

  def draw(self,num_balls_drawn):
    chosen_balls=[]
    if num_balls_drawn>=len(self.contents):
      return self.contents
    for i in range(num_balls_drawn):
      chosen_ball=random.choice(self.contents)
      chosen_balls.append(chosen_ball)
      self.contents.remove(chosen_ball)
    return chosen_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes=0
  for i in range(num_experiments):
    accurate_pred=0
    chosen_balls=copy.deepcopy(hat).draw(num_balls_drawn)
    for key,value in expected_balls.items():
      if chosen_balls.count(key)>=value:
        accurate_pred+=1
    if accurate_pred==len(expected_balls):
      successes+=1
    accurate_pred=0
  return successes/num_experiments
