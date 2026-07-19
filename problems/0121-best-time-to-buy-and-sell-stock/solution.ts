function maxProfit(prices: number[]): number {
    let lowestPrice = prices[0];
    let maxProfit = 0;

    for (let i = 1; i < prices.length; i++) {
        const price = prices[i];

        if (price < lowestPrice) {
            lowestPrice = price;
        } else {
            const profit = price - lowestPrice;

            if (profit > maxProfit) {
                maxProfit = profit;
            }
        }
    }

    return maxProfit;
}
