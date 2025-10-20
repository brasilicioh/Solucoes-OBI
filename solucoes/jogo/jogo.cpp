#include <iostream>

using namespace std;

int main() {
    int par, alice, bob, soma;

    cin >> par >> alice >> bob;
    soma = alice + bob;

    if (soma % 2 == 0) {
        cout << par << "\n";
    } else {
        cout << !par << "\n";
    }
    return 0;
}