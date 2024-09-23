#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//declarations or prototypes
int getInt(int min, int max);
void clear(void);

#define MIN 3
#define MAX 15

int main() {

    int input = getInt(MIN, MAX);
    printf("\nThe input is accepted: %d", input);

    printf("The value address is %d", &input);

    return 0;
}

int getInt(int min, int max) {

    int value=0, keeptrying = 1, rc;
    char after;

    do {
        printf("\nEnter the integer value in the range %d-%d", min, max);
        rc = scanf("%d%c", &value,&after);


        if (rc == 0) {
            printf("\n  Bad Input, Try again... ");
            clear();
        }

        else if (after != '\n') {
            printf("  Trailing buffer, Try again ");
            clear();
        }

        else if (value < min || value > max) {
            printf("The values are out of range, Try again...");
            clear();
        }
        else
            keeptrying = 0;
    } while (keeptrying == 1);

    return value;
}

void clear(void) {

    while (getchar() != '\n') {}
}