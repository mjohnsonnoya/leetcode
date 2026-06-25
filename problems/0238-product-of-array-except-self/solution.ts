function productExceptSelf(nums: number[]): number[] {
    var prefix = 1;
    var postfix = 1;
    const ans = new Array<number>(nums.length).fill(1);
    
    for (let i = 0; i < nums.length; i++)
    {
        ans[i] = ans[i] * prefix;
        ans[nums.length - (i + 1)] = ans[nums.length - (i + 1)] * postfix;
        
        prefix = prefix * nums[i];
        postfix = postfix * nums[nums.length - (i + 1)];
        
    }
    
    return ans;
    
};
