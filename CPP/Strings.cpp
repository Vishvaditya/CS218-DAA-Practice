#include <iostream>
#include <vector>
#include <string>

using namespace std;

string generateString(int k) {
    string out_string;
    if (k == 1) {
        out_string = "ABC";
        return out_string;
    } else {
        out_string = "A" + generateString(k-1) + "B" + generateString(k-1) + "C";
    }
    return out_string;
}

string ABCStrings(const string& str, int l, int r) {
    return str.substr(l, r-l);
}

void main_func(int k, int l, int r) {
    string s = generateString(k);
    string output = ABCStrings(s, l-1, r);
    cout << output << endl;
}

int inp() {
    int x;
    cin >> x;
    return x;
}

vector<int> inlt() {
    int k, l, r;
    cin >> k >> l >> r;
    return {k, l, r};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t = inp();
    for (int i = 0; i < t; i++) {
        vector<int> inp_ls = inlt();
        int k = inp_ls[0];
        int l = inp_ls[1];
        int r = inp_ls[2];
        main_func(k, l, r);
    }
    
    return 0;
}