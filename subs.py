s = "GGTGGGTTTCGATGGGTTTGTGGGTTTATGGGTTTAGGGCCGAATGGGTTTCTGTGGGTTTATGGGTTTCAAAGATGGGTTTCAGCTGGGTTTTGGGTTTGAGGTGGGTTTTGTGGGTTTGTGGGTTTCGTGGGTTTGTCGCCTGGGTTTGGTTGGGTTTAGAATACGTTGTTTGGGTTTTGGGTTTGACTGGGTTTAGTGGGTTTATATGGGTTTGCGCTGTTGGGTTTCAGCGTTAGTGGGTTTGTGGGTTTATAATCATGGGTTTCGGCCTCTGGGTTTGCATGGGTTTCTTTGGGTTTGTGGGTTTTGGGTTTGTTGGGTTTGACTGGGTTTGTATGTGGGTTTTGGGTTTTTGGGTTTTGTGGGTTTGTCCTGGGTTTTTGGGTTTCTGTGGGTTTGGGTACCGATGGGTTTTGGGTTTTGGGTTTATGGGTTTTGGGTTTGTGTCACCCTGGGTTTCTGGGTTTTTGGGTTTAATGGGTTTCACATGGGTTTCATGGGTTTTGGGTTTTTGGGTTTGTGGGTTTTGCGTGGGTTTACAATGGGTTTGTCCTGGGTTTGGGCTGGGTTTCTGGGTTTTGGGTTTTATTGGGTTTTGGGTTTCACTGGGTTTCTTGGGTTTTTTCAACCGACGTGGGTTTTGGGTTTGTTCGTGGGTTTCGTGGGTTTCCATAAATGGGTTTTTGGGTTTGAAACCTGGGTTTCTTGGGTTTGTTGGGTTTGTCGTTGGGTTTTGGGTTTGTGGGTTTGTGGGTTTATGGGTTTATTGGGTTTATTGGGTTTACCAATGGGTTTTGGGTTTAGGGTGGGTTTGCTGGGTTTGCTTGGGTTTTGGGTTTTGGGTTTTAGGGCTGGGTTTGTGGGTTTTGGGTTTTTGGGTTTCGCTTCCCTCAGGTGGGTTTTGGGTTTGTGGGTTTCGTGGGTTTAAGAATCAGTGTGGGTTTCTGGGTTTTTCTGGGTTTGTGGGTTT"
t = "TGGGTTTTG"
positions = ""

for j in range(len(s) - 4):
    if s[j:j+len(t)] == t:
        positions += str(j+1) + " "
        
print positions