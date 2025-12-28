class Solution:
    def solve(self,n,A,B,C,cnt):
        if n==1:
            cnt[0]=cnt[0]+1
            return cnt
        self.solve(n-1,A,C,B,cnt)
        self.solve(1,A,B,C,cnt)
        self.solve(n-1,B,A,C,cnt)
        
        
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        cnt=[0]
        self.solve(n,fromm,to,aux,cnt)
        return cnt[0]