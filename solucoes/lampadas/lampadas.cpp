#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int qtdClick, lam1 = 0, lam2 = 0;
    cin >> qtdClick;

    vector<int> clicks(qtdClick);
    for (int i = 0; i < qtdClick; i++) {
        cin >> clicks[i];
    }

    for (auto i: clicks) {
        if (i == 1) {
            lam1 = !lam1;
        } else {
            lam1 = !lam1;
            lam2 = !lam2;
        }
    }

    cout << lam1 << "\n" << lam2 << "\n";

    return 0;
}