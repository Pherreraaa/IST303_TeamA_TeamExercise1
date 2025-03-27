from problem5_code import parse_time_expression

def test_parse_time_expression():
    # Test standard 12-hour formats
    assert parse_time_expression("3:30pm") == (15, 30), "Failed for input '3:30pm'"
    assert parse_time_expression("12:00 AM") == (0, 0), "Failed for input '12:00 AM'"
    assert parse_time_expression("12:00 PM") == (12, 0), "Failed for input '12:00 PM'"

    # Test special expressions
    assert parse_time_expression("midnight") == (0, 0), "Failed for input 'midnight'"
    assert parse_time_expression("noon") == (12, 0), "Failed for input 'noon'"

    # Test phrases
    assert parse_time_expression("quarter past three") == (3, 15), "Failed for 'quarter past three'"
    assert parse_time_expression("half past 7") == (7, 30), "Failed for 'half past 7'"
    assert parse_time_expression("quarter to midnight") == (23, 45), "Failed for 'quarter to midnight'"

    # Test 24-hour formats
    assert parse_time_expression("14:45") == (14, 45), "Failed for input '14:45'"

    # Test hour-only formats
    assert parse_time_expression("3") == (3, 0), "Failed for input '3'"
    assert parse_time_expression("five") == (5, 0), "Failed for input 'five'"

    # Test invalid format returns None
    assert parse_time_expression("random string") is None, "Failed for input 'random string'"

    # Test type validation
    try:
        parse_time_expression(123)
        assert False, "Exception not raised for non-string input"
    except Exception as e:
        assert str(e) == "Input must be a string."

    print("All tests passed!")

if __name__ == "__main__":
    test_parse_time_expression()
