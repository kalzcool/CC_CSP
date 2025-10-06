//CC 7th variables practice 
#include <stdio.h>
int main(void){
    char name[50];
    // user input
    printf("What is your name: \n");
    fgets(name, sizeof(name), stdin);

    printf("Hello %s, welcome to your first c program \n", name);

    return 0;
}