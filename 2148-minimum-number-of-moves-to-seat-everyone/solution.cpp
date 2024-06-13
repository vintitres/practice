class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        sort(seats.begin(), seats.end());
        sort(students.begin(), students.end());
        int size = seats.size();
        int sum = 0;
        for (int i = 0; i < size; ++i) {
            sum += abs(seats[i] - students[i]);
        }
        return sum;
        
    }
};
