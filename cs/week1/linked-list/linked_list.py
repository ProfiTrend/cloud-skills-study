# CS - Data Structure - Linked List
# Jennas Lee

class Node:
    num = None
    next = None

    def __init__(self, num):
        self.num = num


class LinkedList:
    head = None

    # insert last node
    def append(self, num):
        # first insert
        if self.head is None:
            self.head = Node(num)

        else:
            cursor = self.head

            # search last node
            while cursor.next:
                cursor = cursor.next

            cursor.next = Node(num)

    def get(self, index):
        count = 0
        node = self.head

        # search index node
        while count < index:
            count += 1
            node = node.next

        return node

    def insert(self, index, num):
        new_node = Node(num)

        # insert head of linked list
        if index == 0:
            new_node.next = self.head
            # change previous head to new node
            self.head = new_node

            return

        else:
            node = self.get(index - 1)

            # swap node
            next_node = node.next
            node.next = new_node
            new_node.next = next_node

    def delete(self, index):
        # delete head node
        if index == 0:
            self.head = self.head.next

            return

        else:
            node = self.get(index - 1)
            node.next = node.next.next


def main():
    print("LINKED LIST")
    # linked list data structure
    linked_list = LinkedList()

    while True:
        print("\n1 : APPEND | 2 : INSERT | 3 : GET | 4 : DELETE | 0 : EXIT")
        cmd_code = int(input("Plz enter a command code... "))

        # exit
        if cmd_code == 0:
            print("EXIT LINKED LIST PROGRAM")
            break

        # append
        elif cmd_code == 1:
            append_num = int(input("Plz enter a number which you append in linked list... "))

            print("APPEND!", append_num)

            linked_list.append(append_num)

        # insert
        elif cmd_code == 2:
            insert_index = int(input("Plz enter a INDEX number which you insert in linked list... "))
            insert_num = int(input("Plz enter a number which you insert in linked list... "))

            print("INSERT!", insert_num, "(INDEX :", insert_index, ")")

            linked_list.insert(insert_index, insert_num)

        # get
        elif cmd_code == 3:
            get_index = int(input("Plz enter a INDEX number which you get in linked list... "))

            print("GET!", linked_list.get(get_index).num, "(INDEX :", get_index, ")")

        # delete
        elif cmd_code == 4:
            delete_index = int(input("Plz enter a INDEX number which you delete in linked list... "))

            linked_list.delete(delete_index)

            print("DELETE! (INDEX :", delete_index, ")")

        # wrong
        else:
            print("YOU ENTER A WRONG NUMBER!")


if __name__ == '__main__':
    main()
