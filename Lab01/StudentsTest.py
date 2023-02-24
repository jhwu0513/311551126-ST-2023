import unittest
import Students

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")
        for name in self.user_name:
            id = self.students.set_name(name)
            self.user_id.append(id)
            self.assertEqual(self.students.name[id],self.user_name[id])
            print(id,self.students.name[id])
        print("\nFinish set_name test")

    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print("\n\nStart get_name test\n\n")
        print("user_id length = ",len(self.user_id),"\nuser_name length = ",len(self.user_name),"\n")
        mex = 0
        while mex in self.user_id:
            mex += 1
        for i in range(len(self.user_name)+1):
            if i < len(self.user_name):
                self.assertEqual(self.students.get_name(self.user_id[i]),self.user_name[self.user_id[i]])
                print("id",self.user_id[i],":",self.user_name[self.user_id[i]])
            else:
                self.assertEqual(self.students.get_name(mex),'There is no such user')
                print("id",mex,": There is no such user")
        print("\nFinish get_name test")
