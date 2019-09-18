from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_returns_error_when_invalid_input(self):
        invalid_inputs = [1, -5, [1,2], '-', 'a']
        for input in invalid_inputs:
            assert checkout_solution.checkout(input) == -1

    # not sure if its better having this as one test? 
    def test_checkout_returns_correct_price(self):
        test_cases = {
            '': 0,
            'a': -1,
            'ABCa': -1,
            'A': 50,
            'AA': 100,
            'AAA' : 130,
            'AAAAA': 200,
            'B' : 30,
            'BB' : 45,
            'BBEE' : 110,
            'ABAA' : 160,
            'AAAAABBEE': 310,
            'AAAAAAAA': 330,
            'EEB': 80,
            'ABCDECBAABCABBAAAEEAA': 665,
            'FFF': 20,
            'FF': 20,
            'HHHHH': 45,
            'HHHHHHHHHH': 80,
            'HHHHHHHHHHHHH': 110,
            'KK': 150,
            'NNN': 120,
            'NNNM': 120,
            'NNNMM': 135,
            'PPPPP': 200,
            'PPPPPPPPPP': 400,
            'QQQ': 80,
            'RRR': 150,
            'RRRQ': 150,
            'QQQRRRQ': 230,
            'UUU': 80,
            'UUAU': 130,
            'VV': 90,
            'VVV': 130,
            'VVVVV': 220
        }
        for k, v in test_cases.items():
            assert checkout_solution.checkout(k) == v