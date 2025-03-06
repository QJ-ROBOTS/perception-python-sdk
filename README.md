# py-qj-robots

[简体中文](https://github.com/QJ-ROBOTS/perception-python-sdk/wiki/%E5%8D%83%E8%AF%80%C2%B7%E6%84%9F%E7%9F%A5%E5%A4%A7%E6%A8%A1%E5%9E%8B) | [EN](https://github.com/QJ-ROBOTS/perception-python-sdk/wiki/QJ-PERCEPTION-MODEL)

千诀机器人Python SDK，提供了强大的机器视觉感知能力，支持2D/3D图像的目标检测、图像分割、属性描述、角度预测、关键点检测和抓取点预测等功能。

## 环境要求

- Python 3.x
- 依赖包：requests>=2.26.0, python-dotenv>=0.19.0

## 安装

```bash
pip install py-qj-robots
```

## 配置

使用SDK前需要配置以下环境变量：

- QJ_APP_ID：应用ID
- QJ_APP_SECRET：应用密钥

您可以点击[此处](https://qj-robots.feishu.cn/share/base/form/shrcnecZCYdlGcMZPLw4DMb09wd)获取应用ID和密钥。

可以通过以下两种方式配置：

1. 创建.env文件：
```
QJ_APP_ID=your_app_id
QJ_APP_SECRET=your_app_secret
```

2. 使用export命令：
```bash
export QJ_APP_ID=your_app_id
export QJ_APP_SECRET=your_app_secret
```

## 快速开始

```python
from dotenv import load_dotenv
from py_qj_robots import Perception
import os

# 加载环境变量
load_dotenv()

# 初始化Perception实例
perception = Perception()

# 执行2D图像检测
result = perception.check_image(
    image_type="2D",
    image_url="http://example.com/image.jpg",
    object_names=["bottle", "cup"]
)
print(f"检测结果: {result}")
```

## API文档

### Perception类

#### check_image
检测图像中的目标物体。

```python
def check_image(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

参数：
- image_type：图像类型，'2D'或'3D'
- image_url：图像URL
- object_names：要检测的物体名称，可以是字符串或字符串列表
- depth_url：3D图像的深度图URL（仅在image_type为'3D'时需要）

#### split_image
分割图像中的目标物体。

```python
def split_image(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

返回值包含：
- boxes：边界框坐标 [x1,y1,x2,y2]
- masks：掩码图像URL和数据
- croppedImagesListBbox：裁剪图像URL
- labels：检测到的物体标签
- scores：置信度分数

#### props_describe
获取图像中物体的属性描述。

```python
def props_describe(image_type: str, image_url: str, object_names: Union[str, List[str]], questions: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### angle_prediction
预测物体的角度。

```python
def angle_prediction(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### key_point_prediction
预测物体的关键点。

```python
def key_point_prediction(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### grab_point_prediction
预测物体的抓取点。

```python
def grab_point_prediction(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### full_perception
执行完整的感知分析，包含所有功能。

```python
def full_perception(image_type: str, image_url: str, object_names: Union[str, List[str]], questions: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

返回值包含所有感知结果，包括：
- angles：角度信息
- boxes：边界框
- masks：分割掩码
- points：关键点
- grasps：抓取点
- answers：属性描述
- 等等

## 更多信息

访问[千诀机器人官网](https://www.qj-robots.com/)了解更多信息。

