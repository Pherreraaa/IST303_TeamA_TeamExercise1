from problem1_code import determine_primes

def test_determine_primes():
    # Test normal case
    assert determine_primes(11) == ([2, 3, 5, 7, 11], 2), "Test case for input 11 failed."
    
    # Test larger input
    assert determine_primes(22) == ([2, 3, 5, 7, 11, 13, 17, 19], 2), "Test case for input 22 failed."

    # Test small input
    assert determine_primes(1) == ([], 0), "Test case for input 1 failed."

    # Test non-integer input
    try:
        determine_primes("string")
        assert False, "Exception was not raised for non-integer input."
    except Exception as e:
        assert str(e) == "Input must be an integer."

    # Test input zero
    assert determine_primes(0) == ([], 0), "Test case for input 0 failed."

    # Test negative input
    assert determine_primes(-5) == ([], 0), "Test case for negative input failed."

if __name__ == "__main__":
    test_determine_primes()
    print("All tests passed!")
