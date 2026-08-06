class MinStack {
    private stack: number[];
    private mins: number[];

    constructor() {
        this.stack = [];
        this.mins = [];
    }

    push(value: number): void {
        this.stack.push(value);
        this.mins.push((this.mins.length === 0) ? value : Math.min(value, this.mins[this.mins.length - 1]));
    }

    pop(): void {
        this.stack.pop();
        this.mins.pop();
    }

    top(): number {
        return this.stack[this.stack.length - 1];
    }

    getMin(): number {
        return this.mins[this.mins.length - 1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
