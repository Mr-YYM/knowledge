// 下面是一个简单的 C 程序，它使用 `open` 和 `read` 系统调用来读取文件的内容，然后用 `write` 系统调用将内容打印到标准输出（即屏幕）：

#include <fcntl.h> // 引入文件控制定义。Include for file control definitions.
#include <unistd.h> // 引入 Unix 标准函数定义。Include for Unix standard function definitions.
#include <stdio.h> // 引入标准 I/O 函数。Include for standard I/O functions.

#define BUFFER_SIZE 1024 // 定义读取文件的缓冲区大小。Define the buffer size for file reading.

int main() {
    char buffer[BUFFER_SIZE]; // 读取文件的缓冲区。Buffer for file reading.
    ssize_t bytesRead; // 已读取的字节数。Number of bytes read.

    // 打开文件。Open the file.
    int fd = open("/root/learn_open.txt", O_RDONLY);
    if (fd == -1) {
        // 打开文件失败，打印错误信息。If fail to open the file, print error message.
        // 这个函数接收一个字符串作为参数，然后将这个**字符串和一个描述最后一次系统错误的错误信息**一起输出到标准错误流（stderr）。
        perror("open"); 
        return 1;
    }

    // 循环读取文件内容，直到文件结束。Loop to read the file content until the end of file.
    while ((bytesRead = read(fd, buffer, BUFFER_SIZE)) > 0) {
        // 将读取的内容写入标准输出。Write the read content to the standard output.
        if (write(STDOUT_FILENO, buffer, bytesRead) != bytesRead) {
            perror("write"); // 写入失败，打印错误信息。If fail to write, print error message.
            return 1;
        }
    }

    // 读取文件失败，打印错误信息。If fail to read the file, print error message.
    if (bytesRead == -1) {
        perror("read");
        return 1;
    }

    // 关闭文件。Close the file.
    if (close(fd) == -1) {
        perror("close"); // 关闭文件失败，打印错误信息。If fail to close the file, print error message.
        return 1;
    }

    return 0;
}
