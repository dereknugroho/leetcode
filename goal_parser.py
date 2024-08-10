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
