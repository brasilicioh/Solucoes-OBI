// Feito por Brasilicio Henrique

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> I(n);
    for (int i = 0; i < n; i++) cin >> I[i];

    unordered_set<int> interval;
    int maxInterval = 0, start = 0;

    for (int i = 0; i < n; i++) {
        while (interval.count(I[i])) {
            interval.erase(I[start]);
            start++;
        }
        interval.insert(I[i]);
        maxInterval = max(maxInterval, i - start + 1);
    }

    cout << maxInterval << "\n";
    return 0;
}

