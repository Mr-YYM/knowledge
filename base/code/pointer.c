#include<stdio.h>

void pointer_increment(int *value) {
    (*value)++;
}

void var_increment(int value) {
    value++;
}

int main() {
    // ============= 学习指针在函数中的传递 =============
    // int x = 10;
    // // pointer_increment(&x);  // 使用指针传递x的地址
    // // printf("%d\n", x);  // 输出11
    // var_increment(x);
    // printf("%d\n", x);

    // ============= 学习指针 =============
    int a = 0x12345678;
    printf("0x%08x\n", a);  // 直接打印 hex 输出。0x12345678
    unsigned char* pa = (unsigned char*) &a;  // 拿到执行 a 的指针，并缩小他的类型。

    printf("0x%08x\n", pa[1]);   // 打印指针，指向第 2 步长的内存中数据

    printf("\n");
    // for 循环打印整个
    int i;
    for (i = 0; i < sizeof(int); i++){
        printf("%d:0x%08x\n", i,pa[i]);
    }

    printf("\n");
    // 也能通过指针移动
    for (i = 0; i < sizeof(int); i++){
        printf("%d:0x%08x\n", i,*pa);  // *pa 和 pa[0] 是等价的，这两种表达式都用于访问指针指向的第一个元素的值。在 C 语言中，表达式 pa[i] 等价于 *(pa + i)。
        pa++;
    }
    return 0;
}