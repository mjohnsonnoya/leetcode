function maxProfit(prices: number[]): number {
    let maxProfit = 0;
    let low = prices[0];

    for (const price of prices) {
        low = Math.min(low, price);
        const profit = price - low;
        maxProfit = Math.max(maxProfit, profit);
    }

    return maxProfit;
};
