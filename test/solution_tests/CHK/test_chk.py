from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_returns_error_when_invalid_input(self):
        invalid_inputs = [1, -5, [1,2]]
        for input in invalid_inputs:
            assert checkout_solution.checkout(input) == -1

    def test_checkout_returns_total_value_for_single_item(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout_returns_total_with_offer_applied(self):
        assert checkout_solution.checkout('A,A,A') == 130

