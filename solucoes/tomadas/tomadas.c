#include <stdio.h>
#include <stdlib.h>

int main() {
    int sum = 0, num;

    for (int i = 0; i < 4; i++)
    {
        scanf("%d", &num);
        sum = sum + num;
    }

    sum = sum - 3;

    printf("%d", sum);

    return 0;
}

