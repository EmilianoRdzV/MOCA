#include <stdio.h>
#include <stdint.h>

int main() {
    float a;
    scanf("%f",&a);
    float x=(3*a)+15;
    float y=(x+3)/(x+1);
    float z=(5*x+7*y)/(a*x*y);

    printf("%.3f",z);

  return 0;
}