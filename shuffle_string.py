class Solution:
    def restore_string(self, s, indices):
        new_string = ''
        new_string_index = 0
        old_string_length = len(s)

        while new_string_index < old_string_length:
            for index, value in enumerate(indices):
                if new_string_index == value:
                    new_string += s[index]
                    new_string_index += 1

        return new_string

# Test cases

sol = Solution()

string1 = 'codeleet'
indices1 = [4, 5, 6, 7, 0, 1, 2, 3]
expected1 = 'leetcode'

string2 = 'abc'
indices2 = [0, 1, 2]
expected2 = 'abc'

string3 = 'aiohn'
indices3 = [3, 1, 4, 2, 0]
expected3 = 'nihao'

string4 = 'aaiougrt'
indices4 = [4, 0, 2, 6, 7, 3, 1, 5]
expected4 = 'arigatou'

string5 = 'art'
indices5 = [1, 0, 2]
expected5 = 'rat'

print(f'Input:    \'{string1}\', {indices1}')
print(f'Output:   \'{sol.restore_string(string1, indices1)}\'')
print(f'Expected: \'{expected1}\'')
print('---')

print(f'Input:    \'{string2}\', {indices2}')
print(f'Output:   \'{sol.restore_string(string2, indices2)}\'')
print(f'Expected: \'{expected2}\'')
print('---')

print(f'Input:    \'{string3}\', {indices3}')
print(f'Output:   \'{sol.restore_string(string3, indices3)}\'')
print(f'Expected: \'{expected3}\'')
print('---')

print(f'Input:    \'{string4}\', {indices4}')
print(f'Output:   \'{sol.restore_string(string4, indices4)}\'')
print(f'Expected: \'{expected4}\'')
print('---')

print(f'Input:    \'{string5}\', {indices5}')
print(f'Output:   \'{sol.restore_string(string5, indices5)}\'')
print(f'Expected: \'{expected5}\'')
