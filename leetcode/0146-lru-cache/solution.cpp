class LRUCache {
    int capacity;
    map<int, int> cache;
    list<int> access_queue;
    unordered_map<int, list<int>::iterator> queue_pos;

    void print_q() {
        for (int x : access_queue) {
            cout << x << " ";
        }
        cout << endl;
    }

    void add_access(int key) {
        auto it = queue_pos.find(key);
        if (it != queue_pos.end()) {
            access_queue.erase(it->second);
        }
        access_queue.push_front(key);
        queue_pos[key] = access_queue.begin();
        //cout << "acc " << key << endl;
        //print_q();

    }

public:
    LRUCache(int capacity) : capacity(capacity) {
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) {
            return -1;
        }
        add_access(key);
        return it->second;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it == cache.end()) {
            if (cache.size() == capacity) {
                int x = access_queue.back();
                //cout << "del " << x << endl;
                access_queue.pop_back();
                queue_pos.erase(x);
                cache.erase(x);
            }
            cache[key] = value;
        } else {
            it->second = value;
        }
        add_access(key);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
