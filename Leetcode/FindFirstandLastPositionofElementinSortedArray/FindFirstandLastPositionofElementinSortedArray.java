class Solution {
    private int getFirstIndex(int[] nums, int target) {
        int left=0, right=nums.length-1, firstIndex=-1;
        while (left<=right) {
            int mid = left+(right-left)/2;

            if (nums[mid]<target)
                left=mid+1;
            else if (nums[mid]>=target) {
                if (nums[mid]==target)
                    firstIndex=mid;
                right=mid-1;
            }
        }
        return firstIndex;
    }

    private int getLastIndex(int[] nums, int target, int first) {
        int left=0, right=nums.length-1, lastIndex=first;
        while (left<=right) {
            int mid = left+(right-left)/2;

            if (nums[mid]<=target) {
                if (nums[mid]==target)
                    lastIndex=mid;
                left=mid+1;
            }
            else if (nums[mid]>target)
                right=mid-1;
        }
        return lastIndex;
    }

    public int[] searchRange(int[] nums, int target) {
        int first;
        if ((first = getFirstIndex(nums, target))<0)
            return new int[]{-1, -1};
        int last = getLastIndex(nums, target, first);
        return new int[]{first, last};
    }
}