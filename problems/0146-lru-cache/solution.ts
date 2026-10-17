class LRUCache {
    cache: Map<number, number>;
    capacity: number;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map<number, number>();
    }

    get(key: number): number {
        
        if (!this.cache.has(key)) {
            return -1;
        }

        const value = this.cache.get(key);

        this.cache.delete(key);

        this.cache.set(key, value);

        return value;
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            this.cache.delete(key);
        }

        if (this.cache.size === this.capacity) {
            this.cache.delete(this.cache.keys().next().value);
        }

        this.cache.set(key, value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
