### 说明
- 用户名密码和机构可以写在config文件中
- 该脚本首次执行会执行登录操作，时间会较长，请耐心等待
- 后续会将session对象保存到session文件中
- 并在session有效期内，实现状态保持

1. 安装依赖
``` shell
pip3 install -r requirements.txt
```
2. 脚本权限
``` shell
chmod +x gencode
```
3. (可选)软连接到bin目录
``` shell
ln -s $(pwd)/gencode /usr/local/bin/gencode
```
4. 执行脚本
``` shell
# 如果没有执行3
./gencode phone
# 如果执行了3
gencode phone
```
