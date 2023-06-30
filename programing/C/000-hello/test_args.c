#include <stdio.h>

// 接收命令行参数的办法
int main(int argc, char *argv[]){
    printf("参数数量是:%d\n", argc);
    for(int i = 0;i < argc ;i++){
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
