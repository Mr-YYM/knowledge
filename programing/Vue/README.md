# Vue

## 安装 Node

### 步骤 1: 使用 Homebrew 安装 Node.js

安装完 Homebrew 后，你可以使用以下命令来安装 Node.js 和 npm（npm 会随 Node.js 一起安装）：

```bash
brew install node
```

这个命令会下载并安装最新版本的 Node.js 和 npm。

### 步骤 2: 验证安装

安装完成后，你可以验证 Node.js 和 npm 是否正确安装。在终端运行以下命令来检查它们的版本：

```bash
node --version
npm --version
```

这些命令会显示你安装的 Node.js 和 npm 的版本，确认它们已经成功安装。

### 步骤 3: 更新 Node.js（可选）

如果未来你需要更新 Node.js，可以简单地再次运行 Homebrew 的安装命令：

```bash
brew update
brew upgrade node
```

这会让 Homebrew 更新其仓库数据并升级 Node.js 到最新版本。

在 macOS 上安装 Vue 3 并启动一个名为 `hello_vue` 的项目涉及几个步骤，主要包括安装 Node.js 和 npm（Node.js 的包管理器），然后使用 Vue CLI 创建并启动项目。以下是详细步骤：

## 安装 Vue

### 步骤 1: 安装 Vue CLI

Vue CLI 是一个命令行工具，用于快速生成 Vue 项目的脚手架。通过 npm 安装 Vue CLI：

```bash
npm install -g @vue/cli
```

### 步骤 2: 创建一个新的 Vue 3 项目

使用 Vue CLI 创建一个新的 Vue 3 项目。在终端中，运行以下命令：

```bash
vue create hello_vue
```

这将启动一个交互式界面，引导你选择创建项目的配置。选择 Vue 3，然后按照提示操作。

### 步骤 3: 进入项目并启动

创建项目后，进入项目目录，并启动开发服务器：

```bash
cd hello_vue
npm run serve
```

这将启动一个本地开发服务器，并且通常会在 `http://localhost:8080` 上运行你的 Vue 应用。

### 步骤 4: 访问你的应用

在浏览器中访问 `http://localhost:8080`，你应该能看到你的 Vue 应用正在运行，通常会显示一个欢迎页面。

### 注意

- 确保你的 macOS 用户具有安装软件的相应权限，如果遇到权限问题，可能需要在命令前添加 `sudo`。
- 如果你的 `8080` 端口已被占用，Vue CLI 会尝试使用另一个端口。注意终端输出中提供的 URL。

以上步骤将帮助你在 macOS 上安装 Vue 3 并启动一个基本的 Vue 应用。