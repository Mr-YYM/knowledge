#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define BUFFER_SIZE 1024 // 定义读取文件的缓冲区大小。

// 编写一个 C 语言程序
// 接受两个命令行参数：源文件的名称和目标文件的名称。
// 你的程序应该打开源文件，读取其内容，然后将这些内容写入到目标文件中。


int main(int argc, char *argv[]){
    // C 语言要用怎样的变量接收字符串
    // 在C语言中，字符串通常被表示为字符数组
    // 注意 `argv[2]` 是一个字符指针，而不是一个初始化列表或者字符串字面量。
    char *read_filename = argv[1];
    char *write_filename = argv[2];

    // 如果源文件无法打开，你的程序应该打印一个错误消息并返回非零值。
    int read_file_fd = open(read_filename, O_RDONLY);
    if (read_file_fd == -1){
        char error_msg[256];
        sprintf(error_msg, "open %s error", read_filename);
        perror(error_msg);
        return 1; // main 函数返回 程序终止
    }

    // 如果目标文件已经存在，你的程序应该询问用户是否要覆盖它。
    // 如果用户选择不覆盖，那么你的程序应该立即退出。
    // 使用 `access()` 函数来检查文件是否存在
    int write_file_fd;
    if(access(write_filename, F_OK) != -1){
        // 非 -1 代表文件存在
        printf("文件已存在, 请问是否覆盖 (y/n)\n");
        char yes_no[32];
        scanf("%s", yes_no);
        if(strcmp(yes_no, "yes") == 0 || strcmp(yes_no, "y") == 0){
            // 覆盖文件
            // O_TRUNC 如果文件已经存在，就将其长度截断为 0
            // S_IRUSR 表示用户读取权限
            // S_IWUSR 表示用户写入权限
            // S_IRGRP 设置了属组用户的读权限，S_IROTH 设置了其他用户的读权限。
            write_file_fd = open(write_filename, O_RDWR|O_CREAT|O_TRUNC, S_IRUSR | S_IWUSR| S_IRGRP | S_IROTH);
            printf("覆盖文件 %s ...\n", write_filename);
        }
        else {
            return 1;
        }
    } else {
        // -1 代表文件不存在
        // O_CREAT 如果文件不存在则创建文件
        // S_IRUSR 表示用户读取权限
        // S_IWUSR 表示用户写入权限
        // S_IRGRP 设置了属组用户的读权限，S_IROTH 设置了其他用户的读权限。
        printf("创建文件文件 %s ...\n", write_filename);
        write_file_fd = open(write_filename, O_RDWR|O_CREAT, S_IRUSR | S_IWUSR| S_IRGRP | S_IROTH);
    }

    if (write_file_fd == -1){
        char error_msg[256];
        sprintf(error_msg, "open %s error", read_filename);
        perror(error_msg);
        return 1; // main 函数返回 程序终止
    }


    // 你的程序应该使用适当大小的缓冲区来一次性读取源文件的一部分内容，
    char readfile_buffer[BUFFER_SIZE];

    // 循环读取文件内容，直到文件结束。
    // 注意检查 `read` 和 `write` 的返回值，以确保读取和写入操作都成功完成。
    ssize_t bytesRead = read(read_file_fd, readfile_buffer, BUFFER_SIZE);
    while (bytesRead > 0){
        printf("bytesRead:%zd\n", bytesRead);
        // 然后将这些内容写入到目标文件中，直到源文件的所有内容都被复制过去。
        ssize_t bytesWritten = write(write_file_fd, readfile_buffer, bytesRead);
        if (bytesWritten != bytesRead) {
            // 错误处理
            perror("write file error"); // 写入失败，打印错误信息。
            return 1;
        }
        bytesRead = read(read_file_fd, readfile_buffer, BUFFER_SIZE);
    }
    printf("%s -> %s\n", read_filename, write_filename);

    // 你的程序在完成文件复制后应该关闭所有打开的文件，并返回 0 表示成功完成。
    close(read_file_fd);
    close(write_file_fd);

    return 0;
}