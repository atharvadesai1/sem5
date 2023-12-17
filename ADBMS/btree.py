from BTrees.IIBTree import IIBTree
import time
btree = IIBTree(order=5)

def select_menu():
    print('BTree Operations:')
    print('1.Insert')
    print('2.Search')
    print('3.Display')
    print('4.Exit')
    return 

try:
    while(True):
        select_menu()
        key = input('Enter your choice: ')
        if(key=='1'):
            num = int(input('Enter the number to be inserted: '))
            insert_start_time = time.time()       
            btree.insert(num,num)
            insert_end_time = time.time()
            print('Number inserted sucessfully!')
            print(f'Insertion time: {round((insert_end_time-insert_start_time)*1000,3)} milliseconds\n')
        elif(key=='2'):
            val = int(input('Enter the number to search: '))
            search_start_time = time.time()
            if(val in btree):
                search_end_time = time.time()
                print('Value found in the tree')
                print(f'Searching time: {round((search_end_time-search_start_time)*1000,3)} milliseconds\n')
        elif(key=='3'):
                print(f'BTree: {list(btree.items())}')
        elif(key=='4'):
            print('BTree Operation Exited!\n')
            break
        else:
            print('Please enter the valid choice!\n')
except KeyboardInterrupt:
    print('\nBTree Operation Exited!\n')



