class Solution {
public:
    /**
     * @param a: an integer array
     * @return: nothing
     */
    void sortIntegers2(vector<int> &a) {
        quickSort(a, 0, a.size() - 1);
    }

    void quickSort(vector<int> &nums, int start, int end){
        if (start >= end) {
            return;
        }
        int left  = start;
        int right = end;
        int mid   = int((start + end) / 2);
        int pivot = nums[mid];

        while (left <= right) {
            while (left <= right && nums[left] < pivot){
                left += 1;
            }
            while (left <= right && nums[right] > pivot){
                right -= 1;
            }
            if (left <= right){
                int tmp = nums[left];
                nums[left] = nums[right];
                nums[right] = tmp;
                left++;
                right--;
            }
        }
        quickSort(nums, start, right);
        quickSort(nums, left, end);
    }
};
