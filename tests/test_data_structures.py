import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual((find_max([1, 30, 5, 10])), 30)
        self.assertEqual((find_max([17, 23, 50, 48, 564, 73])), 564)
        self.assertEqual((find_max([56, 48, 95, 23, 16, 12])), 95)

        self.assertNotEqual((find_max([23, 56, 78, 69, 20])), 20) 

    def test_find_min(self):
        self.assertEqual((find_min([1, 2, 3, 4, 5, 6, 7])), 1)
        self.assertEqual((find_min([17, 15, 0, -5, 3])), -5)
        self.assertEqual((find_min([7948, 1235, 8956, 2002])), 1235)

        self.assertNotEqual((find_min([2, 56, 541, 89, 5])), 541)

    def test_find_average(self):
        self.assertEqual((find_average([2, 2, 2, 2, 2])), 2.0)
        self.assertEqual((find_average([1, 2, 3, 4, 5])), 3.0)
        self.assertEqual((find_average([86, 76, 50, 100])), 78.0)

        self.assertNotEqual((find_average([15, 20, 25, 30])), 10.0)

    def test_find_all_even_numbers(self):
        self.assertEqual((find_even_numbers([2, 2, 2, 2, 2])), (2, 2, 2, 2, 2))
        self.assertEqual((find_even_numbers([1, 2, 3, 4, 5])), (2, 4))
        self.assertEqual((find_even_numbers([86, 76, 50, 100])), (86, 76, 50, 100))

        self.assertNotEqual((find_even_numbers([25, 147, 86, 91, 78])), (147, 156))

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([6, 7, 8, 9, 0]), (7, 9))
        self.assertEqual(find_odd_numbers([12, 56, 43, 94, 39]), (43, 39))
        self.assertEqual(find_odd_numbers([1998, 1956, 1888, 2024]), ())

        self.assertNotEqual(find_odd_numbers([1, 3, 5, 7, 9, 11]), ())

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual((find_number_of_even_numbers([2, 4, 6, 8, 10])), 5)
        self.assertEqual((find_number_of_even_numbers([25, 78, 56, 90, 91, 53])), 3)
        self.assertEqual((find_number_of_even_numbers([1, 9, 13, 7, 25, 5])), 0)

        self.assertNotEqual(find_number_of_even_numbers([10, 20, 30, 50, 40]), 4)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 3, 5, 6, 7, 9]), 5)
        self.assertEqual(find_number_of_odd_numbers([]), 0)
        self.assertEqual(find_number_of_odd_numbers([23, 30, 71, 15, 56, 78, 39]), 4)

        self.assertNotEqual(find_number_of_odd_numbers([1, 19, 3, 28, 12]), 5)

    def test_return_list_stats(self):
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), {  "unique_numbers": {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
                                                                                "min": 1, "max": 10, "average": 5.5,
                                                                                "even_numbers": (2, 4, 6, 8, 10),
                                                                                "odd_numbers": (1, 3, 5, 7, 9),
                                                                                "number_of_even_numbers": 5,
                                                                                "number_of_odd_numbers": 5
                                                                            })
        
        self.assertEqual(return_list_stats([2002, 600, 453, 7600, 4500]), {'unique_numbers': {453, 7600, 2002, 4500, 600},
                                                                            'min': 453,
                                                                            'max': 7600,
                                                                            'average': 3031.0,
                                                                            'even_numbers': (2002, 600, 7600, 4500),
                                                                            'odd_numbers': (453,),
                                                                            'number_of_even_numbers': 4,
                                                                            'number_of_odd_numbers': 1
                                                                            })
        
        self.assertEqual(return_list_stats([750, 345, 365, 434, 676]), {'unique_numbers': {750, 345, 365, 434, 676},
                                                                            'min': 345,
                                                                            'max': 750,
                                                                            'average': 514.0,
                                                                            'even_numbers': (750, 434, 676),
                                                                            'odd_numbers': (345, 365),
                                                                            'number_of_even_numbers': 3,
                                                                            'number_of_odd_numbers': 2
                                                                            })
        
        self.assertNotEqual(return_list_stats([2000, 2000, 200, 20, 20, 2]), {'unique_numbers' : {240,},
                                                                            'min': 2,
                                                                            'max': 2000,
                                                                            'average': 707,
                                                                            'even_numbers': (2000, 2000, 200, 20, 20, 2),
                                                                            'odd_numbers': (345, 365),
                                                                            'number_of_even_numbers': 3,
                                                                            'number_of_odd_numbers': 2})
    
    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        list2 = ["z", "10", "b", "20", "y", "30", "c", "40"]
        result_alphabets, result_numbers = process_characters(input_list)
        
        self.assertEqual(process_characters(input_list), (['a', 'b', 'c', 'd', 'e'], [1, 3, 5]))
        self.assertEqual(process_characters(list2), (['b', 'c', 'y', 'z'], [10, 20, 30, 40]))

        self.assertEqual(process_characters(list2), (["b", "c", "y", "z"], [10, 20, 30, 40]))
        self.assertNotEqual(process_characters((["s", "t", "y", "z", "1", "1"])), (["s", "t", "y", "z"], ["1", "1"]))

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        list2 = ["z", "2", "4", "&", "s", "y", "100", "t", "z", "&"]
        list3 = ["b", "k", "6", "*", "w", "6", "*", "9"]
        result_alphabets, result_numbers = process_characters(input_list)

        self.assertEqual(process_characters(list2), (['s', 't', 'y', 'z'], [2, 4, 100]))
        self.assertEqual(process_characters(input_list), (['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 5]))

        self.assertNotEqual(process_characters(list3), (["b" ,"k", "*", "w", "*"], ["6", "6", "9"]))
        

    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        new_list = ["a", "a", "b", "b", "c"]
        result_alphabets, result_numbers = process_characters(input_list)

        self.assertEqual(process_characters(input_list), (["a", "b", "c"], [1]))
        self.assertEqual(process_characters(new_list), (["a", "b", "c"], []))

        self.assertNotEqual(process_characters(["1", "2", "1", "3"]), (["1", "1", "2", "3"]))

    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        new_list = ["1", ")", "&", "\\", "]", "y", "~"]
        result_alphabets, result_numbers = process_characters(input_list)

        self.assertEqual(process_characters(input_list), ([], [1, 2, 3]))
        self.assertEqual(process_characters(new_list), (["y"], [1]))

        self.assertNotEqual(process_characters(["1", "^", "@", "|", ";"]), (["^", "@", "|", ";"], ["1"]))

    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)

        self.assertEqual(process_characters(input_list), (["x"], [4, 6, 8]))
        self.assertEqual(process_characters(["##", "!", "$", "!!", "~", "`", ":", "{"]), ([], []))

        self.assertNotEqual(process_characters(input_list), (["%",  '&', '*', '(', ')', '!', "x"], ["4", "6", "8"]))

    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        assert generate_squared_dict(2) == {1 : 1, 2 : 4}
        assert generate_squared_dict(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
        
        assert generate_squared_dict(100) != {1: 1, 2: 4, 3: 9, 97: 9409, 98: 9604, 99: 9801, 100: 10000}

    def test_convert_word_list_sentence(self):
        
        assert convert_to_word_list(" All clouds have souls.") == ["all", "clouds", "have", "souls."]
        assert convert_to_word_list("The boat was like a pea floating in a great bowl of blue soup, that's how small the resort was")  == ['the', 'boat', 'was', 'like', 'a', 'pea', 'floating', 'in', 'a', 'great', 'bowl', 'of', 'blue', 'soup', 'thats', 'how', 'small', 'the', 'resort', 'was']
        assert convert_to_word_list("I wanna got to the movie, wanna tag along?") == ['i', 'wanna', 'got', 'to', 'the', 'movie', 'wanna', 'tag', 'along?']

        assert convert_to_word_list("The quick brown fox jumps over the lizard") !=  ['the ', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lizard']

    def test_convert_word_list_spaces(self):
        assert convert_to_word_list("The pink p a nther") == ["the", "pink", "p", "a", "nther"]
        assert convert_to_word_list("               The main reason we      tuck shirts is to look neat  ") == ["the", "main", "reason",  "we", "tuck", "shirts", "is", "to", "look", "neat"]
        assert convert_to_word_list("HP computers are fresh hence they are faster             ") == ["hp", "computers", "are", "fresh", "hence", "they", "are", "faster"]

    def test_letters_count_sentence(self):
        assert letters_count_map("yes I am okay") == {'a': 2, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 1, 'j': 0, 'k': 1, 'l': 0, 'm': 1, 'n': 0, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 1, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 2, 'z': 0}
        assert letters_count_map("The car was moving at high speeds") == {'a': 3, 'b': 0, 'c': 1, 'd': 1, 'e': 3, 'f': 0, 'g': 2, 'h': 3, 'i': 2, 'j': 0, 'k': 0, 'l': 0, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 0, 'r': 1, 's': 3, 't': 2, 'u': 0, 'v': 1, 'w': 1, 'x': 0, 'y': 0, 'z': 0}
        assert letters_count_map("The markets are up, you can trade") == {'a': 4, 'b': 0, 'c': 1, 'd': 1, 'e': 4, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 1, 'l': 0, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 0, 'r': 3, 's': 1, 't': 3, 'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 1, 'z': 0}

        assert letters_count_map("liquity is one of the most important thing in trading") != {'a': 2, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 1, 'j': 0, 'k': 1, 'l': 0, 'm': 1, 'n': 0, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 1, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 2, 'z': 0}

    def test_alphanumeric_1(self):
        assert text_to_morse("I love my woman") == "..   .-.. --- ...- .   -- -.--   .-- --- -- .- -."

    def test_alphanumeric_2(self):
        assert text_to_morse("the password is my name and initials") == "- .... .   .--. .- ... ... .-- --- .-. -..   .. ...   -- -.--   -. .- -- .   .- -. -..   .. -. .. - .. .- .-.. ..."
    
    def test_alphanumeric_3(self):
        assert text_to_morse("Frankenstein") != "..-. .-. .- -. -.- . -. .. - . . -."
    
if __name__ == "__main__":
    unittest.main()
