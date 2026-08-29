class TimeMap {
    dictionary:  Map<string, [number, string][]>;
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
        const values = this.dictionary.get(key);
        let l = 0;
        let r = values.length - 1;

        while (l < r) {
            // console.log("l: ", l);
            // console.log("r: ", r);
            const m = Math.ceil((l + r) / 2);
            // console.log("m: ", m);
            if (values[m][0] > timestamp) {
                r = m - 1;
            }

            else {
                l = m;
            }
        }
        return (values[r][0] <= timestamp) ? values[l][1] : "";
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
