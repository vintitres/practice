class LRUCache {
    int capacity;
    list<pair<int,int>> access_queue;
    unordered_map<int, list<pair<int, int>>::iterator> queue_pos;

    void add_access(unordered_map<int,list<pair<int,int>>::iterator>::iterator it, int key, int val) {
        if (it == queue_pos.end()) {
            if (queue_pos.size() == capacity) {
                auto back = access_queue.back();
                access_queue.pop_back();
                queue_pos.erase(back.first);
            }
            access_queue.push_front({key, val});
            queue_pos[key] = access_queue.begin();
        } else if (it->second == access_queue.begin()) {
            it->second->second = val;
            return;
        } else if (it != queue_pos.end()) {
            access_queue.erase(it->second);
            access_queue.push_front({key, val});
            it->second = access_queue.begin();
        }
    }

public:
    LRUCache(int capacity) : capacity(capacity) {
    }
    
    int get(int key) {
        auto it = queue_pos.find(key);
        if (it == queue_pos.end()) {
            return -1;
        }
        assert(it->second->first == key);
        int val = it->second->second;
        add_access(it, key, val);
        return val;
    }
    
    void put(int key, int value) {
        auto it = queue_pos.find(key);
        add_access(it, key, value);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
