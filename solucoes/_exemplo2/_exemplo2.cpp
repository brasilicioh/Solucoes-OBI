// Exemplo de uso do repositório: concatenação de n textos
// teste com: "python validar.py _exemplo2.cpp" no terminal

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    string output = "";
    for (int i = 0; i < n; ++i) {
        string text;
        cin >> text;
        output += text;
    }

    cout << output << "\n";
}