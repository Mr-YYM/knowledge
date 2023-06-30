# 文件 IO

## open

这个系统调用用于打开一个文件。它需要一个文件名和一个或多个标志（如只读，只写，或读写等）作为参数，然后返回一个文件描述符，该描述符将用于后续的 I/O 操作。

例子：
```c
int fd = open("test.txt", O_RDONLY);
if (fd == -1) {
    // 错误处理
}
```

在这段代码中：

`open` 是一个函数，它接收两个参数：一个文件名和一组标志。在这个例子中，文件名是 "test.txt"，标志是 `O_RDONLY`，表示我们只打算读取这个文件。

`open` 尝试打开指定的文件，并返回一个文件描述符。文件描述符是一个非负整数，用于在后续的系统调用（如 `read`, `write`, `close`）中代表这个文件。

如果 `open` 成功，它将返回一个文件描述符。但是如果出现错误（例如，文件不存在，或者我们没有足够的权限来读取这个文件），`open` 将返回 `-1`。因此，我们需要检查 `open` 的返回值来确定文件是否成功打开：

```c
if (fd == -1) {
    // 错误处理
}
```

在这个例子中，如果 `fd` 等于 `-1`，那么我们就知道 `open` 调用失败了。在实际的程序中，我们会在这里添加错误处理的代码，例如打印一条错误消息或退出程序。

这是一个非常基础的 `open` 调用的例子。实际上，`open` 还有更多的标志和选项，可以用来控制如何打开和操作文件。例如，我们可以使用 `O_WRONLY` 或 `O_RDWR` 来以只写或读写模式打开文件，使用 `O_CREAT` 来在文件不存在时创建文件，等等。你可以在 `open` 的手册页中找到完整的信息。


### O_RDONLY 等文件标志（oflag）

这些是定义在 `<fcntl.h>` 头文件中的宏，是 `open` 系统调用的访问模式标志。当你调用 `open` 函数时，你可以使用这些标志来指定如何访问文件。以下是每个标志的解释：

1. **O_RDONLY**：这个标志表示打开一个只读的文件，你可以从这个文件中读取数据，但不能写入数据。它的值是 `0x0000`。

2. **O_WRONLY**：这个标志表示打开一个只写的文件，你可以向这个文件写入数据，但不能从中读取数据。它的值是 `0x0001`。

3. **O_RDWR**：这个标志表示打开一个可读写的文件，你既可以从这个文件中读取数据，也可以向其中写入数据。它的值是 `0x0002`。

4. **O_ACCMODE**：这个标志是一个掩码，用于检查文件的访问模式。它的值是 `0x0003`，这是 `O_RDONLY`、`O_WRONLY` 和 `O_RDWR` 的值的组合。当你想检查一个文件的访问模式时，可以使用这个标志来和文件的状态进行按位与操作。

这些标志可以单独使用，也可以和其他的 `open` 标志一起使用，例如 `O_CREAT`（如果文件不存在则创建文件）和 `O_APPEND`（在写入数据时总是追加到文件的末尾）。在调用 `open` 函数时，你可以使用位运算符 `|` 来组合多个标志。例如，如果你想打开一个可读写的文件，如果文件不存在则创建它，你可以这样写：

```c
int fd = open(filename, O_RDWR | O_CREAT);
```


## read

这个系统调用从一个已打开的文件中读取数据。它需要一个文件描述符、一个缓冲区和一个大小作为参数，然后返回实际读取的字节数。

例子：
```c
char buffer[256];
ssize_t bytesRead = read(fd, buffer, sizeof(buffer) - 1);
if (bytesRead == -1) {
    // 错误处理
}
buffer[bytesRead] = '\0'; // 假设这是一个文本文件
```


## write

这个系统调用将数据写入到一个已打开的文件中。它需要一个文件描述符、一个缓冲区和一个大小作为参数，然后返回实际写入的字节数。

例子：
```c
const char* message = "hello, world";
ssize_t bytesWritten = write(fd, message, strlen(message));
if (bytesWritten == -1) {
    // 错误处理
}
```

## close

这个系统调用关闭一个已打开的文件。关闭文件后，相关的文件描述符就不能再被用于读写操作。

例子：
```c
if (close(fd) == -1) {
    // 错误处理
}
```

## lseek

这个系统调用改变一个已打开文件的当前读/写位置。它需要一个文件描述符、一个偏移量和一个参考点（如文件开始，当前位置，或文件结束）作为参数。

例子：
```c
if (lseek(fd, 0, SEEK_SET) == -1) {
    // 错误处理
}
```