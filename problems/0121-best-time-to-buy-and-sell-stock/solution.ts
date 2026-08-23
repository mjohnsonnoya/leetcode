function maxProfit(prices: number[]): number {
    const n = prices.length;
    let min = prices[0];
    let maxProfit = 0;
    for (let r = 0; r < n; r++) {
        const currPrice = prices[r];

        if (currPrice < min) {
            min = currPrice;
        }

        const profit = currPrice - min;
        maxProfit = Math.max(maxProfit, profit);
    }

    return maxProfit;
};
