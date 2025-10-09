//CC 7th silly sentances
#include <stdio.h>
#include <string.h>

int main(void){

    char name[50];
    printf("Give me a name:\n");
    scanf("%s\n", name);

    int num;
    printf("Give me a number:\n");
    scanf("%d\n", num);

    char noun[50];
    printf("Give me a noun:\n"); 
    scanf("%s\n",noun);

    printf("%s..... why would I ever want to give someone %d %s.That could horrible for their health.\n", name,num, noun);



    return 0;
}