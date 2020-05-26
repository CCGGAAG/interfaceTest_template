# interfaceTest_template
接口自动化测试框架

### 安装依赖库：
在当前项目目录下，运行命令：  
pip install -r requirements.txt

### 更新依赖库：
1. 首先安装pipreqs库：  
pip install pipreqs
2. 在当前项目目录下运行  
pipreqs ./ --encoding=utf-8  
成功会显示：INFO: Successfully saved requirements file in ./requirements.txt


##### 接口自动化引擎设计思路：
1. 底层方法统一化：建立底层方法，兼容不同平台、不同配置和运行入口。
2. 基础配置自动化：对接开发人员文档平台，自动读取接口的配置信息。
3. 运行入口多元化：使用多种维护入口，实现不同方式来调用、组合接口。
4. 校验方式简单化：整合常规校验形式，优化为公共方法，实现快速检测。

##### 接口自动化引擎特点：
1. 简单：使用代码和office不同的调用入口，能够让不同编程水平的测试人员同时进行协作任务。
2. 效率：解放测试人员的接口对接环节，可以将更多精力用于用例设计。
