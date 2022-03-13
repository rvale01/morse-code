import unittest
import morse
import heap
import ham_radio
import tree

class TestMorse(unittest.TestCase):
    # encode
    def test_encode_1(self):
        self.assertEqual( morse.encode('us'), '..- ...')
    def test_encode_2(self):
        self.assertEqual( morse.encode('hello'), '.... . .-.. .-.. --')
    def test_encode_3(self):
        self.assertEqual( morse.encode('check'), '-.-. .... . -.-. -.-')
    def test_encode_4(self):
        self.assertEqual( morse.encode('what'), '.-- .... .- -')
    def test_encode_5(self):
        self.assertEqual( morse.encode('message'), '-- . ... ... .- --. .')

    # decode
    def test_decode_1(self):
        self.assertEqual( morse.decode('..- ...'), 'usss')
    def test_decode_2(self):
        self.assertEqual( morse.decode('-.-. --- -.. .. -. --'), 'coding')
    def test_decode_3(self):
        self.assertEqual( morse.decode('.--. -.-- - .... --- -.'), 'python')
    def test_decode_4(self):
        self.assertEqual( morse.decode('.-- --- -. -.-'), 'work')
    def test_decode_5(self):
        self.assertEqual( morse.decode('.--. .-.. .- -.--'), 'play')

    # symbols
    def test_symbols(self):
        self.assertEqual( morse.encode('hello?'), '.... . .-.. .-.. --- ..--.')

    # heap
    def test_heap_1(self):
        self.assertEqual(heap.decode_bt('-.-. --- -.. .. -. --.'), 'coding')
    def test_heap_2(self):
        self.assertEqual(heap.decode_bt('.-- --- -. -.-'), 'work')

    # ham_radio
    def test_ham_radio_1(self):
        self.assertEqual(ham_radio.encode_ham("r1", "s1", "hi"), ".-. .---- -.. . ... .---- -...- .... .. -...- -.--.")
    def test_ham_radio_2(self):
        self.assertEqual(ham_radio.decode_ham(".-. .---- -.. . ... .---- -...- .... .. -...- -.--."), ("r1", "s1", "hi"))


    def test_empty_tree(self):
        testing_tree = tree.Node()
        self.assertEqual(testing_tree.isEmpty(), True)
    
    # testing insert function and not empty tree
    def test_insert(self):
        testing_tree = tree.Node()
        testing_tree.insert("E", ".")
        self.assertEqual(testing_tree.isEmpty(), False)

    # testing find function
    def test_insert(self):
        testing_tree = tree.Node()
        testing_tree.insert("E", ".")
        self.assertEqual(testing_tree.find("E"), True)

    # testing delete function
        testing_tree = tree.Node()
        testing_tree.insert("E", ".")
        testing_tree.delete("E")
        self.assertEqual(testing_tree.isEmpty(), True)


if __name__ == '__main__':
    unittest.main()