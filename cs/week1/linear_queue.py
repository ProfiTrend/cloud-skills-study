# CS - Data Structure - Queue(Linear Queue)
# Jennas Lee

class LinearQueue:
    queue_array = []
    front = 0
    back = 0

    def enqueue(self, enqueue_num):

        self.queue_array.append(enqueue_num)
        self.back += 1

    def dequeue(self):

        # queue is empty
        if self.front == self.back:
            return ''

        # queue is not empty
        else:
            self.front += 1
            return self.queue_array[self.front - 1]


def main():
    print("LINEAR QUEUE")
    # queue data structure
    queue = LinearQueue()

    while True:
        print("\n1 : ENQUEUE | 2 : DEQUEUE | 0 : EXIT")
        cmd_code = int(input("Plz enter a command code... "))

        # exit
        if cmd_code == 0:
            print("EXIT QUEUE PROGRAM")
            break

        # enqueue
        elif cmd_code == 1:
            enqueue_num = int(input("Plz enter a number which you enqueue in queue... "))

            print("ENQUEUE!", enqueue_num)

            queue.enqueue(enqueue_num)

        # dequeue
        elif cmd_code == 2:
            dequeue_num = queue.dequeue()

            # empty
            if dequeue_num == '':
                print("THERE'S NO NUMBER TO DEQUEUE!")

            # not empty
            else:
                print("DEQUEUE!", dequeue_num)

        # wrong
        else:
            print("YOU ENTER A WRONG NUMBER!")


if __name__ == '__main__':
    main()
