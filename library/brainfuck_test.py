import unittest
import brainfuck

class TestBrainfuckLibrary(unittest.TestCase):
    def test_clean(self):
        output      = brainfuck.clean("++++[>++++<-]>.,.")
        expectation = "++++[>++++<-]>.,."

        self.assertEqual(output, expectation)

    def test_clean_with_comment(self):
        output      = brainfuck.clean("++++ First line\n[ Second line\n> Third line\n++++ Fourth line\n< Fifth line \n- Sixth line\n] Seventh line\n> Eighth line\n.,. Last line")
        expectation = "++++[>++++<-]>.,."

        self.assertEqual(output, expectation)

if __name__ == "__main__":
    unittest.main()
