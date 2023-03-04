import unittest
from unittest.mock import Mock,patch
from app import Application

class ApplicationTest(unittest.TestCase):

    def setUp(self):
        # stub
        Application.__init__ = Mock(return_value=None)
        self.mock = Application()
        self.mock.people = ["William", "Oliver", "Henry", "Liam"]
        self.mock.selected = ["William", "Oliver", "Henry"]
        pass
    
    def fake_mail(self,people):
        ret = []
        for i in range(len(people)):
            ret.append("Congrats," + people[i] + "!")
        return ret

    @patch("app.MailSystem.send")
    @patch("app.MailSystem.write")
    @patch("app.Application.get_random_person")
    def test_app(self,rand_one,Mail_write,Mail_send):
        # mock
        rand_one.side_effect = ["William", "Oliver", "Henry", "Liam"]
        one = self.mock.select_next_person()
        self.assertEqual(one,"Liam")
        print(one,"selected")
        # spy
        Mail_write.side_effect = self.fake_mail([" William", " Oliver", " Henry", " Liam"])
        self.mock.notify_selected()
        for i in self.mock.selected:
            print("Congrats, "+i+"!")
        print("\n\n")
        print(Mail_write.call_args_list)
        print(Mail_send.call_args_list)
        self.assertEqual(Mail_write.call_count,len(self.mock.selected))
        self.assertEqual(Mail_send.call_count,len(self.mock.selected))
        pass


if __name__ == "__main__":
    unittest.main()