
const vector<string> thousands({"Thousand", "Million", "Billion"}); // ... more
const vector<string> tens({"Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                           "Seventy", "Eighty", "Ninety"});
const vector<string> smallnumbers({"One", "Two", "Three", "Four", "Five", "Six",
                                   "Seven", "Eight", "Nine", "Ten", "Eleven",
                                   "Twelve", "Thirteen", "Fourteen", "Fifteen",
                                   "Sixteen", "Seventeen", "Eighteen",
                                   "Nineteen"});
const string hundred = "Hundred";
const string zero = "Zero";

class Solution {
public:
    vector<string> thousandsToWords(int num) {
        vector<string> words;
        assert(num >= 0 && num < 1000);
        int hundreds = num / 100;
        if (hundreds > 0) {
            words.push_back(smallnumbers[hundreds - 1]);
            words.push_back(hundred);
        }
        num %= 100;
        if (num > 0 && num <= 19) {
            words.push_back(smallnumbers[num - 1]);
        } else if (num >= 20) {
            words.push_back(tens[num / 10 - 2]);
            num %= 10;
            if (num > 0) {
                words.push_back(smallnumbers[num - 1]);
            }
        }
        return words;
    }
    void extend(vector<string>& v, vector<string> const& v_prime) {
        v.reserve(v.size() + distance(v_prime.begin(), v_prime.end()));
        v.insert(v.end(), v_prime.begin(), v_prime.end());
    }
    string numberToWords(int num) {
        if (num == 0) {
            return zero;
        }
        vector<string> words;
        for (int tho = 0; num > 0; ++tho) {
            auto w = thousandsToWords(num % 1000);
            if (num % 1000 != 0 && tho > 0) {
                w.push_back(tho <= thousands.size() ? thousands[tho - 1]
                                                   : "10^" + to_string(tho * 3));
            }
            extend(w, words);
            words = w;
            num /= 1000;
        }

        return std::accumulate(
            std::next(words.begin()), 
            words.end(), 
            words[0], 
            [](std::string a, std::string b) {
                return a + " " + b;
            }
        );
    }
};

