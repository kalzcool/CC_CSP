// CC 7th strings notes
#include <stdio.h>
#include <string.h>

int main(void){
    char name[] = "Andrew";

    char last_name[25];
    printf("Tell me your last name: \n");
    scanf("%s", last_name); 
    char full_name[50];
    printf("[%s]\n", full_name);
    strcat(full_name, name);
    printf("[%s]\n", full_name);

    printf("%c\n", last_name[0]);
    last_name[0] = 'R';


    strcat(full_name, " ");
    printf("[%s]\n", full_name);

    strcat(full_name, last_name);
    printf("[%s]\n", full_name);

    printf("Your name is %s %s\n", name, last_name);
    printf("%zu\n", strlen(name));
    printf("%zu\n", sizeof(name));

    return 0;
}