#include <iostream>
using namespace std;

int main() {
    int n, valor, targetValue, finalPosition = 0;

    cin >> n;
    cin >> targetValue;

    for (int i = 1; i < n; ++i) {
        cin >> valor;
        if (valor < targetValue) {
            ++finalPosition;
        }
    }

    cout << finalPosition << endl;

    return 0;
}
