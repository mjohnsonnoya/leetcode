class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        fst = False
        snd = False
        trd = False
        for triplet in triplets:
            if (triplet[0] <= target[0] 
                and triplet[1] <= target[1]
                and triplet[2] <= target[2]):
                if triplet[0] == target[0]:
                    fst = True
                if triplet[1] == target[1]:
                    snd = True
                if triplet[2] == target[2]:
                    trd = True
        if not (fst and snd and trd):
            return False
        return True
        


