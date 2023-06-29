#include <unistd.h>

int main() {
    char buffer[128];
    ssize_t len = read(STDIN_FILENO, buffer, sizeof(buffer));
    write(STDOUT_FILENO, buffer, len);
    return 0;
}

