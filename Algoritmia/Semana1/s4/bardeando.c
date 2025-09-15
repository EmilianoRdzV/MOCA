#include <stdio.h>
#include <stdint.h>

int main() {
    int p,n;
    int suma=0;
    int lect;
    scanf("%d %d",&p,&n);
    for(int i=0; i<n; i++){
        scanf("%d",&lect);
        suma+=lect;
    }
    if(suma>p){
        printf("%d",0);
    }else{
        printf("%d",p-suma);
    }

  return 0;
}
