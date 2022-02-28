import unittest
import morse
import heap
# import tree

class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        # encode
        self.assertEqual( morse.encode('us'), '..- ...')
        self.assertEqual( morse.encode('hello'), '.... . .-.. .-.. --')
        self.assertEqual( morse.encode('check'), '-.-. .... . -.-. -.-')
        self.assertEqual( morse.encode('what'), '.-- .... .- -')
        self.assertEqual( morse.encode('message'), '-- . ... ... .- --. .')

        # decode
        self.assertEqual( morse.decode('..- ...'), 'usss')
        self.assertEqual( morse.decode('-.-. --- -.. .. -. --'), 'coding')
        self.assertEqual( morse.decode('.--. -.-- - .... --- -.'), 'python')
        self.assertEqual( morse.decode('.-- --- -. -.-'), 'work')
        self.assertEqual( morse.decode('.--. .-.. .- -.--'), 'play')

        # symbols
        self.assertEqual( morse.encode('hello?'), '.... . .-.. .-.. --- ..--.')

        # heap
        self.assertEqual(heap.decode_bt('-.-. --- -.. .. -. --.'), 'coding')
        self.assertEqual(heap.decode_bt('.-- --- -. -.-'), 'work')


if __name__ == '__main__':
    unittest.main()