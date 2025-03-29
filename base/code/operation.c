// bit operation

#include<stdio.h>

int main() {
    // int result = 0x123456 & 0x0000ff;
    // printf("The result in decimal     is: %d\n", result);
    // printf("The result in hexadecimal is: %x\n", result);

    // ============= 学习 mask =============

    // int a = ~0; // better than 0xFFFFFFFF, more portable
    // printf("The result in hexadecimal is: %x\n", a);
    // printf("The result in hexadecimal is: %x\n", 0xff & 0x87654321);
    int x = 0x87654321;
    // bad   0xFFFFFF00 should be ~0xFF
    // int b = (0xFF & x) + (~x & 0xFFFFFF00);
    // printf("The result in hexadecimal is: %x\n", b);
    // int c = (0xFFFFFF00 & x) + 0xFF;
    // printf("The result in hexadecimal is: %x\n", c);
    // // great
    // int d = x ^ ~0xFF;
    // printf("The result in hexadecimal is: %x\n", d);
    // int e = x | 0xFF;
    // printf("The result in hexadecimal is: %x\n", e);
    // x ^ 0xFF... 操作，相当于对 x 进行了取反操作。因为 0 ^ 1 = 1, 1 ^ 1 = 0
    // int f = ~x;
    // int g = x ^ ~0;
    // int h = x ^ ~0xFF;  // x ^ 0 则保持原样.
    // printf("The result in hexadecimal: f is %x and g is %x and h is %x\n", f, g, h);

    // ============= 学习 overflow (passive) =============
    // unsigned char i = 255;
    // unsigned char j = i + 1;
    // printf("The result in hexadecimal is: %x\n", j);
    // printf("The result in decimal is: %d\n", j);

    // ============= 学习 overflow (negative) =============
    char k = 127;
    char l = k + 2;
    printf("The result in hexadecimal is: %x\n", l);
    printf("The result in decimal is: %d\n", l);

    return 0;
}