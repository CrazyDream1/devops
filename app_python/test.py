import unittest
import datetime
import time
from web_app import HelloWorld

class TestState(unittest.TestCase):

    def test_check_time_static(self):

        self.app = HelloWorld()
        timezone = datetime.timezone(datetime.timedelta(hours=3))
        current_time = datetime.datetime.now(tz=timezone).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(self.app.index(), current_time)
        
    def test_check_time_difference_dynamic(self):

        self.app = HelloWorld()
        timezone = datetime.timezone(datetime.timedelta(hours=3))
        current_time1 = datetime.datetime.now(tz=timezone).strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(2)
        current_time2 = datetime.datetime.now(tz=timezone).strftime('%Y-%m-%d %H:%M:%S')
        current_time1 = str(current_time1[:-2]) + str(current_time1[-2:] + 2)
        self.assertEqual(current_time1, current_time2)

if __name__ == "__main__":
    unittest.main()