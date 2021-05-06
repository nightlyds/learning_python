import unittest
import sys

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('loo'.upper(), 'LOO')

    def test_isupper(self):
        self.assertTrue('LOO'.isupper())
        self.assertFalse('Loo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # Check, s.split doen`t work if divider is`t a string
        with self.assertRaises(TypeError):
            s.split(2)

class SimpleWidgetTestCase(unittest.TestCase):
    # calls before every test
    def setUp(self):
        pass

    # calls after every test
    def tearDown(self):
        pass

class MyTestCase(unittest.TestCase):

    # just skip
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # skip if something
    @unittest.skipIf(True,
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    # skip only if
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

class ExpectedFailureTestCase(unittest.TestCase):
    # wait for an error
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            # Failed subtests list: (i=1), (i=3), (i=5)
            # without subTest executing will stop after the first error
            # and to identify the error will be harder
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


test_suit_impl = unittest.TestSuite()
test_suit_impl.addTest(unittest.makeSuite(TestStringMethods))
test_suit_impl.addTest(unittest.makeSuite(SimpleWidgetTestCase))
test_suit_impl.addTest(unittest.makeSuite(MyTestCase))
test_suit_impl.addTest(unittest.makeSuite(MySkippedTestCase))
test_suit_impl.addTest(unittest.makeSuite(ExpectedFailureTestCase))

print("count of tests: " + str(test_suit_impl.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suit_impl)

# if __name__ == '__main__':
#     unittest.main()