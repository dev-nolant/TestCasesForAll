import unittest
import user_file_merge as user_file, original_merge as original
import random

temp_array = []

class SolutionCheck():

    def __init__(self):
        super().__init__()
        self.case = 0
        
    def gene(self):
        self.i = 0
        #print("Generating")
        while self.i in range(10):
            temp_array.append(random.randint(1, 100))
            self.i += 1
        
    def original(self):
        #print("Confronting server code")
        self.arr = temp_array
        self.original_test = original.solution(self.arr)

    def test_r(self):
        #print("Confronting user code")
        self.arr = temp_array
        try:
            self.user_test = user_file.solution(self.arr)
        except Exception as client_error:
            return str(client_error)

    def run_check(self):
        self.gene()
        self.test_r()
        self.original()
        try:
            if self.user_test == self.original_test:
                return True
            else:
                return False
        except Exception as server_error:
            return str(server_error)

    def test_first(self):
        while self.case in range(4):
            if len(temp_array) < 1:
                if self.run_check() == True:
                    self.case += 1
                    print("Test Case Passed: ", self.case, end="\nArray after: "+str(temp_array)+"\n-------------------------------------------\n")
                else:
                    self.case += 1
                    print("Test Case Failed: ", self.case, end="\nArray after: "+str(temp_array)+"\n-------------------------------------------\n")
                    print("ERROR :: >> "+str(self.test_r()))
            else:
                temp_array.clear()
                self.test_first()

if __name__ == '__main__':
    SolutionCheck().test_first()