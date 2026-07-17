function maxProfit(prices: number[]): number {
    if (prices.length <= 1) {return 0};
    let maxprofit = 0;
    let buy = prices[0];
    for (const price of prices) {
        buy = Math.min(buy, price);
        maxprofit = Math.max(maxprofit, price - buy);
    }

    return maxprofit;
};
