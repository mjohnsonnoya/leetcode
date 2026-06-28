function productExceptSelf(nums: number[]): number[] {
    var prefix = 1;
    var postfix = 1;
    const ans = new Array(nums.length).fill(1);
    
    for (let i = 0; i < ans.length; i++){
        const j = (ans.length - i - 1);
        ans[i] *= prefix;
        ans[j] *= postfix;
        
        prefix *= nums[i];
        postfix *= nums[j];
    }
    
    return ans;
    
};
