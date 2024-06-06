class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int hand_size = hand.size();
        if (hand_size % groupSize != 0) {
            return false;
        }
        multiset<int> hand_set(hand.begin(), hand.end());
        int groups = hand_size / groupSize;
        for (int i = 0; i < groups; ++i) {
            int first_card = *hand_set.begin();
            hand_set.erase(hand_set.begin());
            for (int j = 1; j < groupSize; ++j) {
                auto it = hand_set.find(first_card + j);
                if (it == hand_set.end()) {
                    return false;
                }
                hand_set.erase(it);
            }
        }
        return true;
    }
};
