class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.next  = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            cap = MIN_CAPACITY
        else:
            cap = capacity
        
        self.capacity     = cap
        self.stored_items = 0
        self.store        = [ None ] * cap


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.stored_items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # reference: http://www.isthe.com/chongo/tech/comp/fnv/

        # 64 bit offset_basis
        hash = 14695981039346656037

        # 64 bit FNV_prime
        prime = 1099511628211

        # encode key to string bytes
        sb = key.encode()

        for b in sb:
            hash *= prime
            hash ^= b
        
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash = 5381
        
        # ord() returns unicode int
        for char in key:
            hash *= 33
            hash += ord( char )
        
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # self.store[ self.hash_index( key ) ] = value
        # self.stored_items += 1

        ndx = self.hash_index( key )

        if self.store[ ndx ] is None:
            self.store[ ndx ] = HashTableEntry( key, value )
            self.stored_items += 1
        else:
            existing = self.store[ ndx ]

            while existing.next and existing.key != key:
                existing = existing.next

            if existing.key == key:
                existing.value = value
            else:
                existing.next = HashTableEntry( key, value )
                self.stored_items += 1

        if self.get_load_factor() > 0.7:
            self.resize( self.capacity * 2 )

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # self.store[ self.hash_index( key ) ] = None
        # self.stored_items -= 1

        ndx  = self.hash_index( key )
        itm  = self.store[ ndx ]
        prev = None
        
        if itm.key == key:
            if itm.next:
                self.store[ ndx ] = itm.next
            else:
                self.store[ ndx ] = None
        else:
            while itm is not None:
                if itm.key == key:
                    break
                prev = itm
                itm  = itm.next
            
            if itm is None:
                print( f'Key "{key}" not found!')
            else:
                prev.next = itm.next


        if self.get_load_factor() < 0.2 and self.capacity > MIN_CAPACITY:
            new_size = self.capacity / 2

            self.resize( new_size )

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        ndx = self.hash_index(key)
        itm = self.store[ ndx ]

        while itm:
            if itm.key == key:
                return itm.value
            else:
                itm = itm.next
                
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        if new_capacity < MIN_CAPACITY:
            cap = MIN_CAPACITY
        else: 
            cap = new_capacity

        self.capacity = cap
        old_store     = self.store
        self.store    = [ None ] * cap
        
        for ndx in range( len( old_store ) ):
            itm = old_store[ ndx ]
            while itm: 
                self.put( itm.key, itm.value )
                itm = itm.next
        
        old_store = None


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
