class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    int binarySearch(vector<int> &nums, int target) {
        // write your code here
        if (nums.size() == 0) {return -1;}
        int start = 0;
        int end = nums.size() - 1;
        while (start + 1 < end){
            int mid = int ((start + end) / 2);
            if (nums[mid] >= target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (nums[start] == target) {return start;}
        if (nums[end] == target) {return end;}
        return -1;        
    }
};
