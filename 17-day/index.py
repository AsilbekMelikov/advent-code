def calculate():
    def generate_num(diff):
        if diff < 0:
            return 8 - abs(diff)
        elif diff == 0:
            return 8
        elif diff > 0:
            return diff
    def run_program(registers, program):
        """
        Simulates the 3-bit computer program.

        Args:
            registers: A dictionary containing initial register values {'A': int, 'B': int, 'C': int}.
            program: A list of integers representing the program.

        Returns:
            A comma-separated string of outputs generated by the program.
        """
        # Unpack initial register values
        A, B, C = registers['A'], registers['B'], registers['C']
        
        # Helper to resolve operands
        def resolve_operand(op):
            if op <= 3:  # Literal values
                return op
            elif op == 4:  # Register A
                return A
            elif op == 5:  # Register B
                return B
            elif op == 6:  # Register C
                return C
            else:  # Invalid operand (7)
                raise ValueError("Invalid combo operand: 7")

        # Initialize the instruction pointer and output list
        output = []
        ip = 0
        # while ",".join(map(str, output)) != ",".join(map(str, program)):

        while ip < len(program):
            # Fetch opcode and operand
            opcode = program[ip]
            operand = program[ip + 1] if ip + 1 < len(program) else None

            # Process instructions
            if opcode == 0:  # adv
                A //= 2 ** resolve_operand(operand)

            elif opcode == 1:  # bxl
                B ^= operand  # Literal operand

            elif opcode == 2:  # bst
                B = resolve_operand(operand) % 8

            elif opcode == 3:  # jnz
                if A != 0:
                    ip =  operand    # Literal operand
                    continue  # Skip the pointer increment

            elif opcode == 4:  # bxc
                B ^= C  # Operand is ignored

            elif opcode == 5:  # out
                output.append(resolve_operand(operand) % 8)

            elif opcode == 6:  # bdv
                B = A // (2 ** resolve_operand(operand))

            elif opcode == 7:  # cdv
                C = A // (2 ** resolve_operand(operand))

            else:
                raise ValueError(f"Invalid opcode: {opcode}")

            # Move to the next instruction
            ip += 2
        return output
    
# *5 +(8**14)*6 + (8**13)*6
    registers = {'A': 202322936867370 , 'B': 0, 'C': 0}
    program = [2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]
    
    total = 0
    # result = run_program(registers, program) 
    # n = len(result)
    # for i in range(100):
        # i = 1
        # while result[i] != program[i] :
    # registers['A'] += 1
    result = run_program(registers, program) 
    print(result, registers['A'], "result")
    # for _ in range(10000):

    #     if result == program:
    #         print(result, registers['A'], "result")
    #     result = run_program(registers, program) 
    #     registers['A'] -= 1
        # print(result, registers['A'])
        # 203147587365417
    
    # print(result, registers['A'])
    # registers['A'] += 7
    # result = run_program(registers, program)     




        
        # while result[i] != program[i]:
        #     registers['A'] += 8**i    
        #     print(result)
        #     result = run_program(registers, program) 
        

calculate()
  



        
    # print(registers['A'])
    # registe   rs = {'A': 2024  , 'B': 0, 'C': 0}
    # program = [0,3,5,4,3,0]
    # result = run_program(registers, program)
    # n = len(result)
    # m = len(program)
    # i = 0
    # print(result)

    # while i < m and len(result) != len(program):
    #     total = 8
    #     for j in range(i + 1):
    #         diff = generate_num(program[j] - result[j] )
    #         print("diff", diff)
    #         total *=  diff
    #     registers['A'] += total
    #     print(registers['A'])
        
    #     result = run_program(registers, program)
        
    #     i += 1
    #     print(result)




# calculate()
# 34792







# def run_programs(registers, program):

#     A, B, C = registers['A'], registers['B'], registers['C']
#     n = len(program)
#     i = 0

#     def find_number(operand):
#         if operand <= 3:
#             return operand
#         elif operand == 4:
#             return A
#         elif operand == 5:
#             return B
#         elif operand == 6:
#             return C
#     output = []

#     while i < n:
#         print(i)
#         opcode = program[i]
#         operand = program[i+1] if i + 1 < n else None
#         new_operand = find_number(operand)
#         if opcode == 0:
#             A //= 2**new_operand
#         elif opcode == 1:
#             B ^= operand
#         elif opcode == 2:
#             B = new_operand % 8
#         elif opcode == 3:
#             if A != 0:
#                 A = operand
#                 continue
#         elif opcode == 4:
#             B = B ^ C
#         elif opcode == 5:
#             output.append(new_operand % 8)
#         elif opcode == 6:
#             B = A // (2**new_operand)
#         elif opcode == 7:
#             C = A // (2**new_operand)
#         i += 2
#     print(output)
#     return ','.join(map(str, output))

# registers = {'A': 117440, 'B': 0, 'C': 0}
# program = [0,3,5,4,3,0]
# print(run_programs(registers, program))





