from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_returns_error_when_invalid_input(self):
        invalid_inputs = [1, -5, [1,2], '-']
        for input in invalid_inputs:
            assert checkout_solution.checkout(input) == -1

    def test_checkout_returns_0_for_empty_cart(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_returns_total_value_for_single_item(self):
        assert checkout_solution.checkout('a') == 50
    
    def test_checkout_can_handle_caps_and_lower(self):
        inputs = ["a", 'A', 'AB', 'aB', 'Ab']
        for input in inputs:
            assert checkout_solution.checkout(input) != -1

    def test_checkout_returns_total_with_offer_applied(self):
        assert checkout_solution.checkout('aaa') == 130

    def test_checkout_returns_total_with_mixed_offers_and_single(self):
        assert checkout_solution.checkout('abaa') == 160        

    def test_checkout_returns_total_with_mixed_input(self):
        assert checkout_solution.checkout('ABCa') == 150

    def test_checkout(self):
        assert checkout_solution.checkout("AA") == 100
