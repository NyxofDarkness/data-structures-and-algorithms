from hashtable.hashtable import HashTable

def left_join(ht1, ht2):
    hashtable = HashTable(size=1024)
    for pos in ht1:
        if ht2.key.contains(pos.key):
            hashtable.add(ht1.key, ht1[pos.value], ht2[pos.key.value])
        else:
            hashtable.add(ht1.key, ht1[pos.value], "NULL")


        # for word in ht1:
        #     if hashtable.contains(word):
        #         return word
        #     else:
        #         hashtable.add(word, word)
        #         continue
        #         for word2 in ht2:
        #             if hashtable.contains(word2):
        #                 hashtable.add(word, word2.value)