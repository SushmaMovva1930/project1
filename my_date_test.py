import unittest
import my_date 

class MyDateTest(unittest.TestCase):
    
    #is_leao_year
    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))
        
    def test_is_leap_year2(self):
        self.assertTrue(my_date.is_leap_year(2000))
        
    def test_is_leap_year3(self):
        self.assertFalse(my_date.is_leap_year(1759))
        
    def test_is_leap_year4(self):
        self.assertFalse(my_date.is_leap_year(2099))
        
    def test_is_leap_year5(self):
        self.assertTrue(my_date.is_leap_year(2020))
        
        
    #orfinal_data
    
    def test_ordinal_date1(self):
        self.assertEqual(1, my_date.ordinal_date(1997, 1, 1))

    def test_ordinal_date2(self):
        self.assertEqual(352, my_date.ordinal_date(2001, 12, 18))
        
    def test_ordinal_date3(self):
        self.assertEqual(295, my_date.ordinal_date(2020, 10, 21))

    def test_ordinal_date4(self):
        self.assertEqual(59, my_date.ordinal_date(2020, 2, 28))
        
    def test_ordinal_date5(self):
        self.assertEqual(279, my_date.ordinal_date(1984,10,5))




    #days_elapsed
    
    def test_days_elapsed1(self):
        self.assertEqual(8035, my_date.days_elapsed(2001, 12, 18, 2023, 12, 18))
    
    def test_days_elapsed2(self):
        self.assertEqual(1346, my_date.days_elapsed(2020, 2, 20, 2023, 10, 28))
    
    def test_days_elapsed4(self):
        self.assertEqual(27833, my_date.days_elapsed(1947, 8, 15, 2023, 10, 28))
    
    def test_days_elapsed5(self):
        self.assertEqual(366, my_date.days_elapsed(2012,1,1,2013,1,1))
    
    
    #day_of_week
    
    
    
    def test_day_of_week1(self):
        self.assertEqual("Monday", my_date.day_of_week(1753, 1, 1))


    def test_day_of_week2(self):
        self.assertEqual("Saturday", my_date.day_of_week(2023, 10, 28))
        
    def test_day_of_week3(self):
        self.assertEqual("Thursday", my_date.day_of_week(2050, 12, 1))
    
    def test_day_of_week4(self):
        self.assertEqual("Tuesday", my_date.day_of_week(1853, 10, 11))
        
    def test_day_of_week5(self):
        self.assertEqual("Saturday", my_date.day_of_week(2025, 6, 21))
        
        
        
    #to_str
    
    def test_to_str1(self):
        self.assertEqual("Friday, 02 August 2024", my_date.to_str(2024, 8, 2))
        
    def test_to_str2(self):
        self.assertEqual("Wednesday, 31 December 2053", my_date.to_str(2053, 12, 31))
        
    def test_to_str3(self):
        self.assertEqual("Sunday, 04 May 2003", my_date.to_str(2003, 5, 4))
        
    def test_to_str4(self):
        self.assertEqual("Monday, 01 January 1753", my_date.to_str(1753, 1, 1))
        
    def test_to_str5(self):
        self.assertEqual("Saturday, 01 January 2124", my_date.to_str(2124, 1, 1))
        
    

if __name__ == '__main__':
    unittest.main()

