#include <stdio.h>

int main() {
    // 步骤1: 创建并初始化 unsigned char 数组
    unsigned char a[256];
    for (int i = 0; i < 256; i++) {
        a[i] = (unsigned char)i;
    }

    // 步骤2: 使用 char* 指针访问数组
    char* b = (char*)a;

    // 步骤3: 打印数组内容
    for (int i = 0; i < 256; i++) {
        // 打印每个字符的整数值（为避免打印不可见字符）
        printf("%5d ", b[i]);
        if ((i + 1) % 25 == 0) // 每16个数换一行，便于查看
            printf("\n");
    }

    return 0;
}
