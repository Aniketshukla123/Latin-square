class Solution:
   def solve(self, mat):
      ch=set(j for i in mat for j in i)
      m=zip(*mat)
      for i,j in zip(mat,m):
         for c in ch:
            if c not in i or c not in j:
               return False
      return True
ob = Solution()
mat = [["x", "x", "z"],["z", "x", "y"],
["y", "z", "x"]]
print(ob.solve(mat))
