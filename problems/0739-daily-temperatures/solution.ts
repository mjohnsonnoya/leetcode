function dailyTemperatures(temperatures: number[]): number[] {
    const answers: number[] = new Array<number>(temperatures.length).fill(0);
    for (let i = temperatures.length - 1; i >= 0; i--) {
        let k = i + 1;
        while (temperatures[k] <= temperatures[i] && k < temperatures.length) {
            if (answers[k] === 0) {
                k = temperatures.length;
                break;
            }
            k += answers[k];
        }
        if (k === temperatures.length) {
            answers[i] = 0;
        }
        else {
            answers[i] = k - i;
        }
    }

    return answers;
};
