#include <unistd.h>

// 在这个例子中，`STDIN_FILENO` 和 `STDOUT_FILENO` 是标准输入和标准输出的文件描述符。
// `read` 函数从标准输入读取数据到 `buffer`，然后 `write` 函数将这些数据写入到标准输出。
int main() {
    char buffer[128];
    ssize_t len = read(STDIN_FILENO, buffer, sizeof(buffer));
    write(STDOUT_FILENO, buffer, len);
    return 0;
}

