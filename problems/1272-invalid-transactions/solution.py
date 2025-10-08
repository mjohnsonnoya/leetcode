class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        invalid_idx = set()
        grouped = defaultdict(list)

        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            parsed.append([name, int(time), int(amount), city] + [i])

        for name, time, amount, city, i in parsed:
            if amount > 1000:
                invalid_idx.add(i)
            grouped[name].append([name, time, amount, city, i])
        
        for key, value in grouped.items():
            for a in range(len(value) - 1):
                for b in range(a, len(value)):
                    if abs(value[a][1] - value[b][1]) <= 60 and value[a][-2] != value[b][-2]:
                        invalid_idx.add(value[a][-1])
                        invalid_idx.add(value[b][-1])
        
        invalid = []
        for idx in invalid_idx:
            invalid.append(transactions[idx])
        
        return invalid
        

        

        
