function dailyTemperatures(temperatures: number[]): number[] {
    const ans = new Array<number>(temperatures.length).fill(0);
    const n = temperatures.length;

    for (let i = n - 2; i >= 0; i--) {
        let k = i + 1;
        while (k < n && temperatures[k] <= temperatures[i]) {
            if (ans[k] === 0) {
                k = n;
                break;
            }
            else {
                k += ans[k];
            }
        }

        if (k !== n) {
            ans[i] = k - i;
        }
    }

    return ans;
};
