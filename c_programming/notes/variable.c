// CC 7th variables notes 
#include <stdio.h>

int main(void){
    int grade = 95; //4 bytes
    float pi = 3.14; //4 bytes
    double long_pi = 3.145926358; //8 bytes of space
    char letter_grade = 'A'; // 1 byte
    char name[] = "Calix";
    printf("%s did it?", name);
    printf("You have a %d, in the class. That is an %c", grade, letter_grade);
    return 0;
}