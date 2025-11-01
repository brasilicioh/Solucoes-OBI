#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int taco, consultas, estoque = 0;
    vector<bool> tacos(1000001, false);

    cin >> consultas;

    for (int i = 0; i < consultas; i++) {
        cin >> taco;
        if (!tacos[taco]) {
            tacos[taco] = true;
            estoque += 2;
        } else {
            tacos[taco] = false;
        }
    }

    cout << estoque << "\n";

    return 0;
}