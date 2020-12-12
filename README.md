# AppUI_Test_airtest_Demo
### 参考

- airtest https://github.com/AirtestProject/Airtest
- airtest官方文档 https://airtest.readthedocs.io/zh_CN/latest/

### 执行脚本基本指令

- airtest run test_blackjack.air --device Android:/// --log log/

### 问题

- mac在本地部署的环境运行airtest报错：PermissionError: [Errno 13] Permission denied

  - 原因：需要手动赋予adb可执行权限，否则执行脚本时可能遇到上诉错误。

  - 解决方法：

    ```
    cd {your_python_path}/site-packages/airtest/core/android/static/adb/mac
    chmod +x adb
    ```