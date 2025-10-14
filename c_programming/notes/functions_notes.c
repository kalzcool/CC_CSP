//CC 7th functions notes. i dont want to do this guys 
#include <stdio.h> 

void birthday(char* name, int age){
     printf("Happy birthday to you\n");
     printf("Happy birthday to you\n");
     printf("Happy birthday dear %s\n", name);
     printf("Happy birthday to you\n");
     printf("Happy birthday %s you are %d\n", name, age);

}

int mul(int x, int y){
    return x * y; 
}

float get_number(char* type){
    float value;
    printf("how many %s do you have: \n", type);
    scanf("%f", &value);
    return value;
}

int main(void){
   birthday("Berrak", 17);
   birthday("Ezra", 8);
   birthday("Julian", 15);
   int product = mul(8,5);
   printf("%d\n", product);
   printf("%d\n", mul(35,76));
   float pencils = get_number("pencils");
   float notebooks = get_number("notebooks");
   printf("You have %.2f pencils and %.2f notebooks\n", pencils, notebooks);
    return 0;
}