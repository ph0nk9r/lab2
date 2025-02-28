import unittest
from main import HTTP_Requests_parser
from main import search_ipv6_in_text 
from main import get_list_from_file


test_list = [
"1050:0000:0000:0000:0005:0600:300c:326b",
"С пропуском начальных нулей 1050:0:0:0:5:600:300c:326b",
"ff06:0:0:0:0:0:0:c3", 
"1050::::5:600:300c:326b",
"0000:0000:0000:0000:0000:0000:0000:0000"
]


valid_list = [
"1050:0000:0000:0000:0005:0600:300c:326b",
"1050:0:0:0:5:600:300c:326b",
"ff06:0:0:0:0:0:0:c3",
"1050::::5:600:300c:326b",
"0000:0000:0000:0000:0000:0000:0000:0000"
]


valid_list_file = [
"1050:0000:0000:0000:0005:0600:300c:326b",
"С пропуском начальных нулей 1050:0:0:0:5:600:300c:326b",
"dsadsadsadawqewqdas ff06:0:0:0:0:0:0:c3",
"1050::::5:600:300c:326b",
"0000:0000:0000:0000:0000:0000:0000:0000"
]

class TestTandem(unittest.TestCase):
    def test_search_ipv6(self):
        self.assertEqual(search_ipv6_in_text(test_list), valid_list)
        self.assertEqual(search_ipv6_in_text(["11111111", "fasdfqawqfsa", "BB"]), None)
    

    def test_get_list_from_file(self):
        list_tandem = get_list_from_file("test_input.txt")
        self.assertEqual(list_tandem, valid_list_file)
        self.assertEqual(search_ipv6_in_text(list_tandem), valid_list) 


if __name__ == "__main__":
    unittest.main()