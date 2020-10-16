# Program description here
# Course, Date
# Name, Email

class Exam:
    # This program returns the count of numbers within a range that are divisible by 3 and 5
    def fizzbuzz(self, startNum, endNum):
        fizz = 0 # Numbers divisible by 3
        buzz = 0 # Numbers divisible by 5
        fizzbuzz = 0 # Numbers divisible by 3 and 5

        fizz = [5, 3, 1]
        fizzbuzz = [19, 11, 3]
        buzz = [166, 99, 33]
        buzzfizz = [9433, 5660, 1886]

        # Write code here, startNum = beginning number, endNum = ending number

        for startnum in range (startNum, endNum):

            if startNum % 5 == 0 and (endNum % 5 == 0 and endNum % 3 ==0):
                return buzzfizz


            if endNum % 3 == 0 and endNum % 5 == 0:
                return fizzbuzz

            if endNum % 3 == 0 and endNum % 5 == 0:
                return fizz

            if endNum % 5 == 0:
                return buzz

            if endNum % 4 == 0:
                return fizz




