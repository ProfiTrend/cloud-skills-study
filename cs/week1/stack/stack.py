# CS - Data Structure - Stack
# Jennas Lee

class Stack:
    stack_array = []

    def push(self, push_num):
        self.stack_array.append(push_num)

    def pop(self):
        # stack is empty
        if len(self.stack_array) <= 0:
            return ''
        # stack is not empty
        else:
            return self.stack_array.pop()


def main():
    print("STACK")
    # stack data structure
    stack = Stack()

    while True:
        print("\n1 : PUSH | 2 : POP | 0 : EXIT")
        cmd_code = int(input("Plz enter a command code... "))

        # exit
        if cmd_code == 0:
            print("EXIT STACK PROGRAM")
            break

        # push
        elif cmd_code == 1:
            push_num = int(input("Plz enter a number which you push in stack... "))

            print("PUSH!", push_num)

            stack.push(push_num)

        # pop
        elif cmd_code == 2:
            pop_num = stack.pop()

            # empty
            if pop_num == '':
                print("THERE'S NO NUMBER TO POP!")
            # not empty
            else:
                print("POP!", pop_num)

        # wrong
        else:
            print("YOU ENTER A WRONG NUMBER!")


if __name__ == '__main__':
    main()
