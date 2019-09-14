from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_returns_error_when_invalid_input(self):
        invalid_inputs = [1, -5, [1,2]]
        for input in invalid_inputs:
            assert checkout_solution.checkout(input) == -1


