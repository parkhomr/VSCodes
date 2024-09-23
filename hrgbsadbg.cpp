// #include <stdio.h>


// void draw_Rectangle(int width, int heightW, char fill);
// void line(int len, char fill);
// void line_nl(int len, char fill);

// struct Rectangle
// {
//     int width, height;
//     char fill;
// }


// struct Rectangle_getSides() {
//     struct Rectangle Rec;
//     printf("Enter the sides of the Rectnagle: ");
//     scanf("%d, %d, %c", &Rec.width, &Rec.height, &Rec.fill);
//     return Rec;
// }

// int main() {

//     int x = 2;
//     struct Rectangle R;
//     R.width = 40;
//     R.height = 5;
//     R.fill = '+';

//     R.getSides();
//     draw_Rectangle(R.width, R.height, R.fill);

//     return 0;
// }


// void draw_Rectangle(int width, int height, char fill) {
//     line_nl(width, fill);
//     for(int i=0; i<height - 2; i++) {
//         putchar(fill);
//         line(width - 2,' ');
//         printf("%c\n", fill);
//     }
//     line_nl(width, fill);
// }

// void line_nl(int len, char fill) {
//     line(len, fill);
//     putchar('\n');
// }

// void line(int len, char fill) {
//     for(int i=0; i<len; i++){
//         putchar(fill);
//     }
// }

#include <stdio.h>

void draw_rect(int b, int l, char fill);
void line(int len, char fill);
void ln(int len, char fill);

struct Rectangle{
    int l,b;
    char fill;
};

int main(){
    struct Rectangle R;
    R.l = 10;  
    R.b = 40;  
    R.fill = '◉_◉';

    draw_rect(R.b, R.l, R.fill);

    return 0;
}

void draw_rect(int b, int l, char fill){
    ln(b, fill);  // Print the top line
    for(int i = 0; i < l - 2; i++){  // Middle part of the rectangle
        putchar(fill);  // Left side
        line(b - 2, ' ');  // Spaces in the middle
        printf("%c\n", fill);  // Right side
    }
    ln(b, fill);  // Print the bottom line
}

void ln(int len, char fill){
    line(len, fill);
    putchar('\n');
}

void line(int len, char fill){
    for(int i = 0; i < len; i++){  // Draw a line of length `len` with `fill`
        putchar(fill);
    }
}