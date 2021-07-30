def is_Primo(a: int) -> bool:
    count: int = 0
    if a > 1:
        for i in range(1,a + 1):
            if a%i == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False
    else:
        return False

import unittest

class Test_Primo(unittest.TestCase):
    def test_primo_true(self):
        self.assertTrue(is_Primo(2))
        self.assertTrue(is_Primo(3))
        self.assertTrue(is_Primo(5))
        self.assertTrue(is_Primo(7))
        self.assertTrue(is_Primo(19))
        self.assertTrue(is_Primo(29))
        self.assertTrue(is_Primo(47))
        self.assertTrue(is_Primo(43))

    def test_primo_false(self):
        self.assertFalse(is_Primo(1))
        self.assertFalse(is_Primo(4))
        self.assertFalse(is_Primo(6))
        self.assertFalse(is_Primo(24))
        self.assertFalse(is_Primo(50))

if __name__ == '__main__':
    unittest.main()