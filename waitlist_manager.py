# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
#create class    
    def __init__(self):
        self.head = None
#add customer to front of waitlist
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f'{name} to the front of waitlist')
#add customer to end of waitlist
    def add_end(self, name):
        new_node = Node(name)
#if list is empty new node becomes the head
        if self.head is None: 
            self.head = new_node
            print(f'{name} to the end of waitlist')
        current = self.head
        while current.next is not None: 
            current = current.next
        current.next = new_node
        print(f'{name} to the end of waitlist')
#remove name from waitlist
    def remove(self,name):
#if list is empty
        if self.head is None: 
            print(f'{name} not found!')
            return
#removing first name on the waitlist
        if self.head.name == name:
            self.head = self.head.next
            print(f'{name} removed from waitlist')
            return
#print the waitlist
#empty waitlist
    def print_list(self):
        if self.head is None:
            print("waitlist is empty!")
            return
#print waitlist
        current = self.head
        while current is not None: 
            print(current.name)
            current = current.next



def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- My list works by using commands prompted in the terminal (one through five) to add, edit or 
remove customers from the waitlist. Each customer is represented by a node which stores the 
customer’s name and reference to the next node in the list. Once the command is chosen, it 
adds, edits or removes the customer’s name to the list or if the command is to print, it will 
print the current list or if the command is to exit, it will exit the list. In the case where 
there are no matching names and a request to remove a name is commanded, the system will prompt 
that the name isn’t found or if the user is trying to print an empty list, it will advise the 
list is empty and both options will return the user to the main menu. The “head” is the 
beginning of the list, which is where you start when looking for information within a list. 
An engineer might need a custom list like this when the information on a list needs to be 
reorganized and the items on the list can be removed and added. One example that comes to mind 
for me is when I worked at a meat market and I made a list of products that were close to 
expiring. This list changes weekly and can change depending on what we would get on the truck. 
As the product sells, it is removed from the list and as time goes on, more products get added 
to the list and the order can change depending on if we would get a product that is older than 
what we have already or if there is overstock on meat that was already cut. 
'''
