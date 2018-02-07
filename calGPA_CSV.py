class GradeData:
   def __init__(self,subid,name,weigth,grade):
      self.subid = subid
      self.name = name
      self.weigth = int(weigth)
      self.grade = grade
   def getSubid(self):
      return self.subid
   def getName(self):
      return self.name
   def getWeigth(self):
      return self.weigth
   def getGrade(self):
      return self.grade
   def gradetopoint(self):
      if(self.grade == 'A'):
         return 4
      elif(self.grade == 'B+'):
         return 3.5
      elif(self.grade == 'B'):
         return 3
      elif(self.grade == 'C+'):
         return 2.5
      elif(self.grade == 'C'):
         return 2
      elif(self.grade == 'D+'):
         return 1.5
      elif(self.grade == 'D'):
         return 1
      else:
         return 0
   def weigthxpoint(self):
      return self.weigth*GradeData.gradetopoint(self)
   
def setup():
   csv = open('DatabaseP2.csv','r')
   gradeAll = []
   read_grade = cvs.readline()
   for i in read_data:
      line_data = i.strip().split(",")
      data = GradeData(line_data[0],line_data[1],line_data[2],line_data[3])
      gradeAll.append(data)
   print(gradeAll)
   csv.close()
#   print ('{:.2f}'.format(cal_gpa(gradeAll))

#def cal_gpa(gradeAll):
#   sumweigth = 0
#   sumgrade = 0
#   for i range(len(gradeAll)):
#      sumgrade += gradeAll[i].weigthxpoint()
#      sumweigth += gradeAll[i].getWeigth()
#   return sumgrade/sumweigth   

setup()













