import java.util.HashMap;
class Solution {
    HashMap<Integer, Integer> resultDict = new HashMap<Integer, Integer>();

    public int fib(int n) {
        if(this.resultDict.containsKey(n)) return resultDict.get(n);
        if(n<=1) return n;
        else {
            int result = fib(n-1) + fib(n-2);
            this.resultDict.put(n, result);
            return result;
        }
    }

}