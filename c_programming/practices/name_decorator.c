//CC 7th name decorator 
#include <stdio.h>
#include <string.h>

int main(void){

    char first_name[50];
    printf("Tell me your first name:\n");
    scanf("%s", first_name);
    char last_name[50]; 
    printf("Tell me your last name:\n");
    scanf("%s", last_name);
    strcat(first_name, last_name);

    printf("^^%s^^\n",first_name);
   


    return 0; 
}