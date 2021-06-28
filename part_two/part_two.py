from tests import ALG_ONE_TESTS


def get_total_identical_pairs(list_of_numbers):
    """
    Given an array of integers
    Return the amount of "GOOD" pairs in the array
    Where list_of_numbers[a] == list_of_numbers[b] and a < b
    """
    # Add your code here
    return 0


if __name__ == "__main__":
    # The below runs tests found in test.py against your solution in get_total_identical_pairs
    # Uncomment it all until your happy to test
    for test in ALG_ONE_TESTS:
        result = get_total_identical_pairs(
            test.get('list_of_numbers'),
        )
        expected_result = test.get('expected_result')
        assert result == expected_result, "This test expected {} pairs, but it returned {} pairs".format(
            result,
            expected_result,
        )
