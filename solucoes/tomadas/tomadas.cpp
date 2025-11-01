#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T, sum;

    for (int i = 0; i < 4; ++i) {
        cin >> T;
        sum += T-1;
    }

    sum += 1;

    cout << sum << "\n";
    
    return 0;
}
