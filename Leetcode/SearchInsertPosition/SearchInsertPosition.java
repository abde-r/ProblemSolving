class Solution {
    public int searchInsert(int[] nums, int target) {

        int first=0, last=nums.length-1;

        while (first<=last) {
            int mid=first+(last-first)/2;

            if (nums[mid]<target)
                first=mid+1;
            else if (nums[mid]>target)
                last=mid-1;
            else
                return mid;
        }
        return first;
    }
}