# CPU


## 重要概念理解

### 指令集架构

> https://en.wikipedia.org/wiki/Instruction_set_architecture
>
> In computer science, an instruction set architecture (ISA) is an abstract model that generally defines how software controls the CPU in a computer or a family of computers.
>
> 所谓指令集，就是访问 CPU 的接口，所谓 an abstract model that generally defines how software controls the CPU


### 并发（Concurrency）与并行（Parallelism）[1]

简单的人话表达，就是做到计算机能够同时运行不同的任务，因为 CPU 在单个时刻，他只能处理一个指令。如果没有特别设计，电脑用起来，就会这个任务在跑着，别的任务就卡住了。

通常，单个核心的 CPU 在某一时刻，只能执行一个任务。为了实现让计算机能够**同时处理任务**，计算机实现了并发与并行两种能力。**这种能力由操作系统的任务调度（Scheduling）和 CPU 的硬件特性共同实现。**

**并发**是指 CPU（单个核心）在速度极快的交替处理任务的能力，这个交替处理使人看起来就像同时进行那样。 

**并行**是指 CPU 多个核心同时处理多个任务的能力。

并发与并行能够同时存在。

在现代计算机的实现中，可以从操作系统和 CPU 两个角度看待**并发**。

在操作系统层面，通过**进程**来管理一个单位的资源分配（可以理解为一个程序）。操作系统在进程中实现了**线程**，通过它来调度计算资源，因此线程是计算资源调度的基本单位。操作系统能够在单一进程内管理多个线程，在某个时刻，CPU 只能处理一个线程的某个指令，操作系统在极短时间内不断交替的给这些线程分配 CPU 资源，进而实现了并发能力，从用户的感受看，就看起来任务在同时运行。

在 CPU 层面，CPU 能够不断的交替执行不同的任务，这是 CPU 自带的并发能力。（中断指令实现）

用现实的生活作类比，就相当于一条产线上的工人。多个工人在同时生产配件，这叫并行。一个工人，能够交替的制作不同的配件，这叫并发。

> 线程特性由操作系统实现
>
> https://en.wikipedia.org/wiki/Thread_(computing)
>
> In computer science, a thread of execution is the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is typically a part of the operating system

### 深入并发（Concurrency）与并行（Parallelism）

1. 线程资源间的并发，存在上下文切换，这需要消耗额外的时间与资源。（通过时间片轮转和上下文切换实现并发）。协程等用户态线程可减少切换成本。  
2. 高并发服务（如 Web 服务器）通过异步 I/O 管理海量请求。所谓异步（实现上叫协程）是指在单线程内实现了同时处理任务的能力。这种协程只适用于高 IO 的任务，当任务在等 IO，可以让出 CPU 资源给别的任务。这完全是逻辑上的实现，核心实现原：事件循环。Javascript 、Python 协程是具体的实现。
3. 单核 CPU 通过中断、流水线、超线程提升并发效率


## 参考

1. [bilibili: 多核系统上的线程](https://www.bilibili.com/video/BV1vMBLYTEN3?spm_id_from=333.788.videopod.sections&vd_source=8aa37a221241324ded2148d1040b927f)
