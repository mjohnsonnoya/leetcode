class TimeMap {
    store: Map<string, [number, string][]>;
    constructor() {
        this.store = new Map<string, [number, string][]>();
    }

    set(key: string, value: string, timestamp: number): void {
        if (!this.store.has(key)) {
            this.store.set(key, []);
        }

        this.store.get(key).push([timestamp, value]);
    }

    get(key: string, timestamp: number): string {
        if (!this.store.has(key)) {
            return "";
        }

        let l = 0;
        let r = this.store.get(key).length - 1;

        while (l < r) {
            const m = Math.ceil((l + r)/2);

            if (this.store.get(key)[m][0] <= timestamp) {
                l = m;
            }

            else {
                r = m - 1;
            }
        }

        if (r < 0 || this.store.get(key)[r][0] > timestamp) {
            return "";
        }

        return this.store.get(key)[l][1];
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
