class Score(object):
   
   def __init__(self, goal=0, point=0):
      self.goal = goal
      self.point = point

   def __str__(self):
      return "{} goal(s) and {} point(s)".format(self.goal, self.point)

   def score_to_points(self):
      return self.goal * 3 + self.point

   def __eq__(self, other):
      return self.score_to_points() == other.score_to_points()

   def __gt__(self, other):
      return self.score_to_points() > other.score_to_points()

   def __ge__(self, other):
      return self.score_to_points() >= other.score_to_points()

   def __add__(self, other):
      return Score(self.goal + other.goal, self.point + other.point)

   def __sub__(self, other):
      return Score(self.goal - other.goal, self.point - other.point)

   def __iadd__(self, other):
      x = self.goal + other.goal
      y = self.point + other.point
      z = Score(x,y)
      self.goal, self.point = z.goal, z.point
      return self
      
   def __isub__(self, other):
      x = self.goal - other.goal
      y = self.point - other.point
      z = Score(x,y)
      self.goal, self.point = z.goal, z.point
      return self
   
   def __mul__(self, other):
      return Score(self.goal * other, self.point * other)
   
   def __rmul__(self, other):
      return Score(self.goal*other, self.point*other)
      
   def __imul__(self, other):
      x = self.goal * other
      y = self.point * other
      z = Score(x,y)
      self.goal, self.point = z.goal, z.point
      return self
   

def main():

    # Create some instances of Score
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(2, 11)
    s5 = Score(1, 1)

    # Display
    print('Display...')
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # Equality / inequality
    print('Equality / inequality...')
    print(s1 == s2)
    print(s1 != s2)
    print(s2 == s3)
    print(s2 != s3)
    print(s3 == s4)
    print(s3 != s4)

    # Greater than / less than
    print('Greater than / less than...')
    print(s1 > s2)
    print(s2 < s3)

    # Greater than or equal to / less than or equal to
    print('Greater than or equal to / less than or equal to...')
    print(s1 >= s2)
    print(s2 >= s3)
    print(s3 >= s2)
    print(s2 >= s4)
    print(s4 >= s2)
    print(s1 <= s2)
    print(s2 <= s3)
    print(s3 <= s2)
    print(s2 <= s4)
    print(s4 <= s2)

    # Addition
    print('Addition...')
    s6 = s3 + s4
    print(s6)

    # Subtraction
    print('Subtraction...')    
    s6 = s2 - s5
    print(s6)

    # In-place addition
    print('In-place addition...')
    s2alias = s2
    s2 += s5
    print(s2)
    print(s2 > s5)
    print(s2 == s2alias)

    # In-place subtraction
    print('In-place subtraction...')
    s2 -= s5
    print(s2)
    print(s2 > s5)
    print(s2 == s2alias)

    # Sorting
    print('Sorting...')    
    for s in sorted([s1, s2, s3, s4, s5, s6], reverse=True):
        print(s)

if __name__ == '__main__':
    main()
