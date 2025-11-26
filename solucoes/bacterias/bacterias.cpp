#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int bacterias = 1;
    int multiplicador, recipiente;

    cin >> recipiente >> multiplicador;

    int dia = 0;
    while (bacterias <= recipiente) {
        bacterias *= multiplicador;
        dia++;
    }
    dia--;
    cout << dia << "\n";

    return 0;
}