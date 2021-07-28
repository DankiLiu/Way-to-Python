"""THis is a file to reformat the English script from Youtube."""

'''Todo:
    name will also trigger a new line.'''

file = open('cats.txt')
lines = file.readlines()

new_lines = []
for line_index in range(len(lines)):
    new_line = ""
    if line_index != 0:
        if lines[line_index][0].islower():
            new_line = lines[line_index-1].rstrip('\n') + ' '
            print(lines[line_index-1])
        else:
            new_line = lines[line_index-1]
    new_lines.append(new_line)

print(lines)
print(new_lines)
script = ""
for line in new_lines:
    script = script + line
f = open('script', 'w')
f.write(script)
