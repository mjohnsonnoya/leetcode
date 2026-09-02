function dailyTemperatures(temperatures: number[]): number[] {
    const answers: number[] = Array(temperatures.length).fill(0);
    const n = temperatures.length;

    for (let i = n - 2; i >= 0; i--) {
        let k = i + 1;
        while (k < n && temperatures[k] <= temperatures[i]) {
            if (answers[k] === 0) {
                k = n;
            }
            else {
                k += answers[k];
            }
        }
        if (k !== n) {
            answers[i] = k - i;
        }
    }

    return answers;
};
