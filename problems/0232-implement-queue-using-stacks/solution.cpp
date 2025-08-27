class MyQueue {
    private:
        std::vector<int> pushing;
        std::vector<int> popping;
public:
    MyQueue() {
    }
    
    void push(int x) {
        this->pushing.emplace_back(x);
    }
    
    int pop() {
        if  (this->popping.empty()) {
            while (!this->pushing.empty()) {
                 this->popping.emplace_back(this->pushing.back());
                 this->pushing.pop_back();
            }
        }
        int val =  this->popping.back();
        this->popping.pop_back();
        return val;

        
    }
    
    int peek() {
        if (this->popping.empty()) {
            while (!this->pushing.empty()) {
                this->popping.emplace_back(this->pushing.back());
                this->pushing.pop_back();
            }
        }
        return this->popping.back();
    }
    
    bool empty() {
        return (this->pushing.empty() && this->popping.empty());
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
