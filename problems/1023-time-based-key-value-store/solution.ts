class TimeMap {
    dictionary: Map<string, [number, string][]>;
    constructor() {
        this.dictionary = new Map<string, [number, string][]>();
    }

    set(key: string, value: string, timestamp: number): void {
        if (!this.dictionary.has(key)) {
            this.dictionary.set(key, []);
        }
        this.dictionary.get(key).push([timestamp, value]);
    }

    get(key: string, timestamp: number): string {
        if (!this.dictionary.has(key)) {
            return "";
        }

        let l = 0;
        let r = this.dictionary.get(key).length - 1;

        while (l < r) {
            const m = Math.ceil((l + r) / 2);

            if (this.dictionary.get(key)[m][0] > timestamp) {
                r = m - 1;
            }
            else {
                l = m;
            }
        }

        return this.dictionary.get(key)[r][0] <= timestamp ? this.dictionary.get(key)[r][1] : "";
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
