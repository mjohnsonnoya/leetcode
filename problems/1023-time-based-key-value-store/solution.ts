class TimeMap {
    map;
    constructor() {
        this.map = new Map<string, [number, number][]>();
    }

    set(key: string, value: string, timestamp: number): void {
        if (!this.map.has(key)) {
            this.map.set(key, []);
        }

        this.map.get(key).push([value, timestamp]);
    }

    get(key: string, timestamp: number): string {

        if (!this.map.has(key)) return "";
        
        let l = 0;
        let r = this.map.get(key).length - 1;

        while (l < r) {
            const m = Math.ceil((l + r)/2);

            const time: number = this.map.get(key)[m][1];

            if (time <= timestamp) {
                l = m;
            }

            else {
                r = m - 1;
            }
        }

        return (this.map.get(key)[l][1] <= timestamp) ? this.map.get(key)[l][0] : "";
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
