class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = ""
        for f in folder:
            if not prev or not (f.startswith(prev) and f[len(prev)] == '/'):
                result.append(f)
                prev = f
        return result
