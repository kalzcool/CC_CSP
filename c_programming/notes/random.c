//CC 7th getting random num
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void){
	srand(time(NULL));
    char fam[][15] = {"Mama", "Alex", "Dad", "little miss", "Berrak", "Andy", "Anna", "Ryan"};
	
	for(int i=0; i<5; i++){
		int num = rand() %8;
		printf("Our random person is %s\n", fam[num]);
}
    return 0;
}
