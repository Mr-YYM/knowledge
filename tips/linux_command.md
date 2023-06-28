
## find

### 找出特定日期范围的文件

你可以使用 `find` 命令的 `-newermt` 选项来找出在指定日期范围内的文件。这个选项可以找出在给定日期之后修改的文件。然后，你可以使用 `! -newermt` 来找出在给定日期之前修改的文件。这样，你就可以找出在两个日期之间修改的文件。

例如，以下命令会找出在 2023-01-01 到 2023-04-30 之间修改的文件：

```bash
find /path/to/search -type f -newermt 2023-01-01 ! -newermt 2023-04-30
```

你可以使用 `-exec` 选项来对找到的文件执行命令。例如，以下命令会将找到的文件移动到 "archive_202301-202304" 目录：

```bash
find /path/to/search -type f -newermt 2023-01-01 ! -newermt 2023-04-30 -exec mv {} /path/to/archive_202301-202304 \;
```

注意：在这些命令中，你需要将 `/path/to/search` 和 `/path/to/archive_202301-202304` 替换为你实际的搜索路径和目标目录路径。这些命令可能需要相应的权限才能正确执行，你可能需要使用 `sudo`。

另外，请注意，在使用这些命令之前，最好先进行测试以确保它们的行为符合你的期望，特别是在使用 `-exec mv` 选项的时候，因为这可能会覆盖目标目录中的同名文件。