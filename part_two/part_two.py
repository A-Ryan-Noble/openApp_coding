from tests import ALG_ONE_TESTS


def get_total_identical_pairs(list_of_numbers):
    """
    Given an array of integers
    Return the amount of "GOOD" pairs in the array
    Where list_of_numbers[a] == list_of_numbers[b] and a < b
    """

    pairs = 0

    # Loop through the list of number
    for a in range(len(list_of_numbers)):

        # Start from after the first number of the possible pair
        for b in range(a + 1, len(list_of_numbers)):

            # Compare the first pair to next possible number pair
            if list_of_numbers[a] == list_of_numbers[b]:

                # The first number's index must be less than the second number's index
                if a < b:
                    pairs += 1

    return pairs


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
