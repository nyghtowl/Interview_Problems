'''
Object Oriented Programming Practice

Use (or create) a course info class and edx objects. Create the support methods in the edx class to set grades, get grades, set Pset and get Pset. These methods inherit and utilize the courseInfo object methods.


Question on MIT Comp Sci 101 final.

'''

class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"
        
    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))


    def _findCourse(self, course):
        matching_courses = [c for c in self.myCourses if course == c.courseName]
        try:
            return matching_courses[0] 
        except IndexError:
            return None


    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        #   fill in code to set the grade
        course = self._findCourse(course)

        if course:
            course.setGrade(grade)


    def getGrade(self, course="6.02x"):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the grade
        course = self._findCourse(course)

        if course:
            return course.getGrade()
        else:
            return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        course = self._findCourse(course)

        if course:
            return course.setPset(pset, score)


    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset

        course = self._findCourse(course)

        if course:
            return course.getPset(pset)
        else:
            return -1


if __name__ == '__main__':
    #Test section

    edX = edx( ["6.00x","6.01x","6.02x"] )
    edX.setPset(1,100)
    edX.setPset(2,200,"6.00x")
    edX.setPset(2,90,"6.00x")

    edX.setGrade(100)

    for c in ["6.00x","6.01x","6.02x"]:
        edX.setGrade(90,c)
        print edX.getPset(1, c)

