#. Implement a hash table data structure using separate chaining collision resolution.


START

1. Initialize an empty hash table with an array of size N
2. Read input key-value pair (K, V) to insert
3. Calculate hash value for the key K
4. Compute the index of the hash table cell for the calculated hash value
5. Check if the cell is empty
   a. If the cell is empty, create a new linked list and add the key-value pair (K, V) to the head
   b. If the cell is not empty, append the key-value pair (K, V) to the end of the linked list
6. Read input key K to search
7. Calculate hash value for the key K
8. Compute the index of the hash table cell for the calculated hash value
9. Traverse the linked list at the cell and search for the key K
   a. If the key is found, return the corresponding value
   b. If the key is not found, return an error message
10. Read input key K to delete
11. Calculate hash value for the key K
12. Compute the index of the hash table cell for the calculated hash value
13. Traverse the linked list at the cell and search for the key K
   a. If the key is found, remove the corresponding key-value pair from the linked list
   b. If the key is not found, return an error message
14. Repeat steps 2 to 13 until all input key-value pairs have been processed
15. END
