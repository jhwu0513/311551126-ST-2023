import unittest
from unittest.mock import Mock,patch
from course_scheduling_system import CSS

class Test(unittest.TestCase):
    css = CSS()
    course = []

    def test_1_add_course(self):
        # q1_1
        CSS.check_course_exist = Mock(return_value=True)
        self.css.add_course(('Math', 'Monday', 1, 2))
        self.course.append(('Math', 'Monday', 1, 2))
        self.assertEqual(self.css.get_course_list(), self.course)

    def test_2_add_course(self):
        # q1_2
        CSS.check_course_exist = Mock(return_value=True)
        self.css.add_course(('Algorithms', 'Monday', 3, 5))
        self.css.add_course(('OS', 'Monday', 3, 4))
        self.course.append(('Algorithms', 'Monday', 3, 5))
        self.assertEqual(self.css.get_course_list(), self.course)

    def test_3_add_course(self):
        # q1_3
        CSS.check_course_exist = Mock(return_value=False)
        self.css.add_course(('Algorithms', 'Tuesday', 1, 2))
        self.assertEqual(self.css.get_course_list(), self.course)

    def test_4_add_course(self):
        # q1_4
        CSS.check_course_exist = Mock(return_value=False)
        self.assertRaises(TypeError, self.css.add_course, ['Algorithms', 'Tuesday', 1, 2])
        

    @patch("course_scheduling_system.CSS.check_course_exist")
    def test_5_add_course(self,check_course): 
        # q1_5
        CSS.check_course_exist = Mock(return_value=True)
        self.css.add_course(('Algorithms', 'Thursday', 1, 2))
        self.css.add_course(('OS', 'Thursday', 3, 4))
        self.css.add_course(('Data Structure', 'Thursday', 5, 6))
        self.css.remove_course(('OS', 'Thursday', 3, 4))
        self.assertEqual(self.css.remove_course(('OS', 'Thursday', 1, 2)),False)
        self.course.append(('Algorithms', 'Thursday', 1, 2))
        self.course.append(('Data Structure', 'Thursday', 5, 6))
        self.assertEqual(self.css.get_course_list(), self.course)
        # self.assertEqual(check_course.call_count, 4)
        self.css.__str__()

    def test_6_add_course(self): 
        # q1_6
        self.assertRaises(TypeError, self.css.add_course, [['Algorithms'], 'Tuesday', 1, 2])
        self.assertRaises(TypeError, self.css.add_course, ['Algorithms', 'Hello', 1, 2])
        self.assertRaises(TypeError, self.css.add_course, ('Algorithms', 'Tuesday', 1, "2"))
        self.assertRaises(TypeError, self.css.add_course, ('Algorithms', 'Sunday', 1, 2))
        self.assertRaises(TypeError, self.css.add_course, (['Algorithms'], 'Sunday', 1, 2))
        self.assertEqual(self.css.remove_course(('OS', 'Tuesday', 7, 8)),False)
        self.assertEqual(self.css.remove_course(('Data Structure', 'Thursday', 1, 2)),False)
        self.assertEqual(self.css.remove_course(('OS', 'Thursday', 1, 2)),False)
    


