import unittest
from unittest.mock import Mock,patch
from app import Application

# reference : 
# https://medium.com/@henry-chou/%E5%96%AE%E5%85%83%E6%B8%AC%E8%A9%A6%E4%B9%8B-mock-stub-spy-fake-%E5%82%BB%E5%82%BB%E6%90%9E%E4%B8%8D%E6%B8%85%E6%A5%9A-ba3dc4e86d86

class ApplicationTest(unittest.TestCase):
    # 處理相依性的技巧就只分為stub跟mock兩類

    def setUp(self):
        # stub 用來取代相依的物件，但不會驗證輸出是否正確
        Application.__init__ = Mock(return_value=None)
        self.mock = Application()
        self.mock.people = ["William", "Oliver", "Henry", "Liam"]
        self.mock.selected = ["William", "Oliver", "Henry"]
        pass
    
    
    def fake_mail(self,people):
        # fake 只是一個不做任何事的假物件，測試只會經過這個假物件，不會進行任何驗證，所以是個stub
        return "Congrats, " + people + "!"

    @patch("app.MailSystem.send")
    @patch("app.MailSystem.write")
    @patch("app.Application.get_random_person")
    def test_app(self,rand_one,Mail_write,Mail_send):
        # mock 用來驗證與相依物件的互動是否正確
        rand_one.side_effect = ["William", "Oliver", "Henry", "Liam"]
        one = self.mock.select_next_person()
        self.assertEqual(one,"Liam")
        print(one,"selected")
        # spy 如果spy會驗證偽造的方法是否收到正確參數，則spy可以視為mock，如果不驗證參數，而是為了讓偽造的方法回傳需要的結果，則spy可以視為stub
        Mail_write.side_effect = self.fake_mail
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


    