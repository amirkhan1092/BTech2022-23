import java.util.HashMap;
import java.util.Map;

public class two_sum {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int target = 7;
        int[] ans = twoSum(arr, target);
        System.out.println(ans[0] + " " + ans[1]);
    }
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];
        for (int i=0; i<nums.length; i++)
        {
            if (map.containsKey(target - nums[i]))
            {
                ans[0] = map.get(target - nums[i]);
                ans[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        return ans;
    }
}
