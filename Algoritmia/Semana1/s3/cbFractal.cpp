#include <stdio.h>

int main() {
    int n;
    unsigned long long factorial = 1;
    scanf("%d", &n);

    for (int i = 2; i <= n; i++) {
        factorial *= i;
    }

    printf("%llu\n", factorial);

    return 0;
}
