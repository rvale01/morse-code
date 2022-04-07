import morse
import assert_tests


if __name__ == "__main__":
    # This commented code was requested in part 2 in worksheet 2.1
    # e = morse.encode('us')
    # print('%s' % e)
    # d = morse.decode(e)
    # print(d)
    # assert morse.encode('us') == '..- ...', "Should be ..-"
    # assert morse.decode('..- ...') == 'us', "Should be ..-"

    assert_tests.test_encode_us()
    print('Everything passed')