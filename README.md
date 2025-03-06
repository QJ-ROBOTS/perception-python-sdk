# py-qj-robots

千诀机器人Python SDK，提供了强大的机器视觉感知能力，支持2D/3D图像的目标检测、图像分割、属性描述、角度预测、关键点检测和抓取点预测等功能。

QJ Robots Python SDK provides powerful machine vision perception capabilities, supporting object detection, image segmentation, attribute description, angle prediction, keypoint detection, and grasp point prediction for 2D/3D images.

## 环境要求 | Requirements

- Python 3.x
- 依赖包 | Dependencies：requests>=2.26.0, python-dotenv>=0.19.0

## 安装 | Installation

```bash
pip install py-qj-robots
```

## 配置 | Configuration

使用SDK前需要配置以下环境变量：

The following environment variables need to be configured before using the SDK:

- QJ_APP_ID：应用ID | Application ID
- QJ_APP_SECRET：应用密钥 | Application Secret

您可以点击[此处](https://qj-robots.feishu.cn/share/base/form/shrcnecZCYdlGcMZPLw4DMb09wd)获取应用ID和密钥。

You can click [here](https://qj-robots.feishu.cn/share/base/form/shrcnecZCYdlGcMZPLw4DMb09wd) to obtain your Application ID and Secret.

可以通过以下两种方式配置：

You can configure these variables in two ways:

1. 创建.env文件 | Create a .env file:
```
QJ_APP_ID=your_app_id
QJ_APP_SECRET=your_app_secret
```

2. 使用export命令 | Using export command:
```bash
export QJ_APP_ID=your_app_id
export QJ_APP_SECRET=your_app_secret
```

## 快速开始 | Quick Start

```python
from dotenv import load_dotenv
from py_qj_robots import Perception
import os

# 加载环境变量 | Load environment variables
load_dotenv()

# 初始化Perception实例 | Initialize Perception instance
perception = Perception()

# 执行2D图像检测 | Perform 2D image detection
result = perception.check_image(
    image_type="2D",
    image_url="http://example.com/image.jpg",
    object_names=["bottle", "cup"]
)
print(f"检测结果 | Detection result: {result}")
```

## API文档 | API Documentation

### Perception类 | Perception Class

#### check_image
检测图像中的目标物体。

Detect target objects in the image.

```python
def check_image(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

参数 | Parameters：
- image_type：图像类型，'2D'或'3D' | Image type, '2D' or '3D'
- image_url：图像URL | Image URL
- object_names：要检测的物体名称，可以是字符串或字符串列表 | Names of objects to detect, can be a string or list of strings
- depth_url：3D图像的深度图URL（仅在image_type为'3D'时需要）| Depth image URL (required only when image_type is '3D')

#### split_image
分割图像中的目标物体。

Segment target objects in the image.

```python
def split_image(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

返回值包含 | Return value includes：
- boxes：边界框坐标 [x1,y1,x2,y2] | Bounding box coordinates [x1,y1,x2,y2]
- masks：掩码图像URL和数据 | Mask image URLs and data
- croppedImagesListBbox：裁剪图像URL | Cropped image URLs
- labels：检测到的物体标签 | Detected object labels
- scores：置信度分数 | Confidence scores

#### props_describe
获取图像中物体的属性描述。

Get attribute descriptions of objects in the image.

```python
def props_describe(image_type: str, image_url: str, object_names: Union[str, List[str]], questions: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### angle_prediction
预测物体的角度。

Predict object angles.

```python
def angle_prediction(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### key_point_prediction
预测物体的关键点。

Predict object keypoints.

```python
def key_point_prediction(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### grab_point_prediction
预测物体的抓取点。

Predict object grasp points.

```python
def grab_point_prediction(image_type: str, image_url: str, object_names: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

#### full_perception
执行完整的感知分析，包含所有功能。

Perform complete perception analysis, including all features.

```python
def full_perception(image_type: str, image_url: str, object_names: Union[str, List[str]], questions: Union[str, List[str]], depth_url: Optional[str] = None) -> Dict
```

返回值包含所有感知结果，包括：

Return value includes all perception results:
- angles：角度信息 | Angle information
- boxes：边界框 | Bounding boxes
- masks：分割掩码 | Segmentation masks
- points：关键点 | Keypoints
- grasps：抓取点 | Grasp points
- answers：属性描述 | Attribute descriptions
- 等等 | etc.

## 更多信息 | More Information

访问[千诀机器人官网](https://www.qj-robots.com/)了解更多信息。

Visit [QJ Robots Official Website](https://www.qj-robots.com/) for more information.

