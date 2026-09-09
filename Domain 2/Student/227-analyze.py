operands = ['+','-','*','/','//','%']
for operand in operands:
    if operand == '//':
        print('// is a floor division operand')
        break
    print(operand, 'is an operand')