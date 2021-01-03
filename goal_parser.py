class Solution:
    def interpret(self, command):
        parsed = ''
        i = 0

        while i < len(command):
            if command[i] == 'G':
                parsed += 'G'
            elif command[i:i + 2] == '()':
                parsed += 'o'
            elif command[i:i + 4] == '(al)':
                parsed += 'al'
            i += 1

        return parsed

# Test cases

sol = Solution()

command1 = 'G()(al)'
expected1 = 'Goal'

command2 = 'G()()()()(al)'
expected2 = 'Gooooal'

command3 = '(al)G(al)()()G'
expected3 = 'alGalooG'

print(f'Input:    \'{command1}\'')
print(f'Output:   \'{sol.interpret(command1)}\'')
print(f'Expected: \'{expected1}\'')
print('---')

print(f'Input:    \'{command2}\'')
print(f'Output:   \'{sol.interpret(command2)}\'')
print(f'Expected: \'{expected2}\'')
print('---')

print(f'Input:    \'{command3}\'')
print(f'Output:   \'{sol.interpret(command3)}\'')
print(f'Expected: \'{expected3}\'')