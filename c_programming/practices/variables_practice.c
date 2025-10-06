//CC 7th variables practice 
#include <stdio.h>
int main(void){
    char name[50];
    // user input
    printf("What is your name: \n");
    fgets(name, sizeof(name), stdin);

    printf("What is your %s \n", name)
}