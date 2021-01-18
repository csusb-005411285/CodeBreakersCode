class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = S
        permutations = []
        permutations.append(s.lower())
        for i, char in enumerate(s):
            if char.isalpha():
                for j in range(len(permutations)):
                    permutation = list(permutations[j])
                    if permutation[i].isalpha():
                        modified_word = permutation[:i] + [permutation[i].upper()] + permutation[i + 1:]
                        permutations.append(''.join(modified_word))
        return permutations
