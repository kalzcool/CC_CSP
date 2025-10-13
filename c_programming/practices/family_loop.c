//CC 7th family loop 
#include <stdio.h>

int main(void){
    char families[][20]= {"Dad", "Dom", "Little miss", "Mama", "Alex", "Berrack", "Andy", "Anna", "Lexi", "River", "shannel", "Ezra", "Lucas"};
    for(int i=0; i<13; i++){
        printf("Hello, %s\n", families[i]);
    }
    return 0; 
}