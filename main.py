import morse
import assert_tests


if __name__ == "__main__":
    # e = morse.encode('us')
    # print('%s' % e)
    # d = morse.decode(e)
    # print(d)
    # assert morse.encode('us') == '..- ...', "Should be ..-"
    # assert morse.decode('..- ...') == 'us', "Should be ..-"
    assert_tests.test_encode_us()
    print('Everything passed')