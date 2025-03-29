// 打印数据在内存中的实际的存储的样子（十六进制）

#include<stdio.h>
#include<string.h>

typedef unsigned char *byte_pointer;

// void show_bytes(byte_pointer start, int len) {
//     int i;
//     for (i = 0; i < len; i++)
//     {
//         printf(" %.2x", start[i]);
//     }
//     printf("\n");
// }

// void show_int(int x) {
//     show_bytes((byte_pointer) &x, sizeof(int));
// }

// void show_float(float x) {
//     show_bytes((byte_pointer) &x, sizeof(float));
// }

// void show_str(const char *x){
//     show_bytes((byte_pointer) x, strlen(x));
// }

// void show_pointer(void *x) {
//     show_bytes((byte_pointer) &x, sizeof(void *));
// }

int main()
{
    int a = 165535;  // 02 86 9f
    // int* ptr = &a;
    // printf("%d\n", *ptr);  // *ptr  解引用，获取指针对应的值
    unsigned char* b = (unsigned char*) &a;
    printf("%d\n", *b);
}

// typedef unsigned char *byte_pointer;
// 为什么
