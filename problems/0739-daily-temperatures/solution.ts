function dailyTemperatures(temperatures: number[]): number[] {
    let n = temperatures.length;
    const ans: number[] = new Array<number>(temperatures.length).fill(0);
    for (let i = temperatures.length - 2; i >= 0; i--) {
        let k = i + 1;
        while ((temperatures[k] <= temperatures[i]) && (k !== n)) {
            if (ans[k] === 0) {
                k = n;
                break;
            }
            k += ans[k];
        }

        if (k !== n) {
            ans[i] = k - i;
        };
    }
    
    return ans;
};
