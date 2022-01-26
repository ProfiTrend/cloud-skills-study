# CS - Data Structure - Queue(Circular Queue)
# Jennas Lee

class CircularQueue:
    QUEUE_SIZE = 10
    queue_array = list()
    front = 0
    back = 0
    size = 0

    # init queue size
    def __init__(self):
        self.queue_array = list(range(self.QUEUE_SIZE))

    def enqueue(self, enqueue_num):

        # queue is full
        if self.size == self.QUEUE_SIZE:
            return ''

        # queue is not full
        else:
            self.queue_array[self.back] = enqueue_num
            self.back = (self.back + 1) % self.QUEUE_SIZE
            self.size += 1

    def dequeue(self):

        # queue is empty
        if self.size == 0:
            return ''

        # queue is not empty
        else:
            dequeue_num = self.queue_array[self.front]
            self.front = (self.front + 1) % self.QUEUE_SIZE
            self.size -= 1

            return dequeue_num


def main():
    print("CIRCULAR QUEUE")
    # queue data structure
    queue = CircularQueue()

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

            # queue is full
            if queue.enqueue(enqueue_num) == '':
                print("QUEUE IS FULL!")

            # queue is not full
            else:
                print("ENQUEUE!", enqueue_num)

        # dequeue
        elif cmd_code == 2:
            dequeue_num = queue.dequeue()

            # queue is empty
            if dequeue_num == '':
                print("THERE'S NO NUMBER TO DEQUEUE!")

            # queue is not empty
            else:
                print("DEQUEUE!", dequeue_num)

        # wrong
        else:
            print("YOU ENTER A WRONG NUMBER!")


if __name__ == '__main__':
    main()
