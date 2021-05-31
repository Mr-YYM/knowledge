# Jenkins

## jenkinsfile 实用模板

- 通用模板

    ```jenkinsfile
    pipeline {
        agent { label 'dotnet' }

        // 环境变量
        environment  {
            PYPI_HOST = "nexus3.lan.wiqun.com"
        }

        options {
            timeout(time: 10, unit: 'MINUTES') // 超时时间
            retry(1)
            disableConcurrentBuilds()  // 不允许并发构建同一个任务
            buildDiscarder(logRotator(daysToKeepStr: '180', numToKeepStr: '45'))
            ansiColor('xterm')
        }

        parameters {
            string(name: 'STRING', defaultValue: "dev", description: '输入框')
            booleanParam(name: 'BOOLEAN', defaultValue: false, description: '勾选框')
            choice(name: 'CHOICE', choices: ['dev', 'api', 'ui'], description: '下拉框')
        }

        stages {
            // 定义阶段
            stage("stage 1") {
                steps {
                    echo "初始化构建环境..."
                    script {
                        // if 语句
                        if (env.STRING == "abc") {
                            echo "abc"
                        }
                        // 定义变量
                        def extra_args = "abc"
                        // 重试
                        retry(3){
                            // 执行一条 shell 命令
                            sh "python3 demo.py ${extra_args}"
                        }
                    }
                }
            }

            stage('stage 2') {
                steps {
                    script {
                        // 从标准输出读入 json
                        job_info = readJSON text: sh(
                            encoding: 'utf-8',
                            returnStdout: true,
                            script: "python3 demo.py"
                        ).trim()
                        src_git_url = job_info['src_ssh_git_url']
                        project_name = job_info['name']
                        // 从 Jenkins 密钥库拿 ssh key ss
                        sshagent (credentials: ['git-ssh-privatekey']) {
                            sh """
                            python3 demo.oy ${src_git_url}
                            """
                        }
                    }

                }
            }


        }
        // 最后做的事情
        post {
            always {
                echo "清理工作目录..."
                // 任务失败时保留现场
                cleanWs cleanWhenFailure: false, notFailBuild: true
            }
        }
    }


    ```
