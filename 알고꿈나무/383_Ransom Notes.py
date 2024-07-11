class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)> len(magazine):
            return False
        
        ransomnote_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)

        for char, count in ransomnote_count.items():
            magazine_counts = magazine_count[char]
            if magazine_counts < count:
                return False

        return True