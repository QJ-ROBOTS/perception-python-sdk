import os

from dotenv import load_dotenv

from py_qj_robots import Perception


def init_perception():
    # 加载环境变量
    load_dotenv()

    # 检查必要的环境变量
    required_vars = ['QJ_APP_ID', 'QJ_APP_SECRET']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f'缺少必要的环境变量: {", ".join(missing_vars)}')

    # 初始化Perception实例
    return Perception()


def test_2d_image_detection(perception):
    # 测试2D图像检测
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]

    try:
        # 执行图像检测
        result = perception.check_image(
            image_type="2D",
            image_url=image_url,
            object_names=object_names
        )
        print(f"检测结果: {result}")
        return True
    except Exception as e:
        print(f"检测失败: {str(e)}")
        return False


def test_3d_image_validation(perception):
    # 测试3D图像必须提供depth_url
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = "box"

    try:
        perception.check_image(
            image_type="3D",
            image_url=image_url,
            object_names=object_names
        )
        print("错误：期望抛出ValueError异常但未抛出")
        return False
    except ValueError as e:
        print(f"验证成功：正确捕获到异常 - {str(e)}")
        return True
    except Exception as e:
        print(f"验证失败：捕获到意外异常 - {str(e)}")
        return False


def test_2d_image_split(perception):
    # 测试2D图像分割
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]

    try:
        # 执行图像分割
        result = perception.split_image(
            image_type="2D",
            image_url=image_url,
            object_names=object_names
        )
        print(f"分割结果: {result}")
        return True
    except Exception as e:
        print(f"分割失败: {str(e)}")
        return False


def test_2d_image_props_describe(perception):
    # 测试2D图像属性问答
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]
    questions = ["这个物体是什么颜色的？"]

    try:
        # 执行属性问答
        result = perception.props_describe(
            image_type="2D",
            image_url=image_url,
            object_names=object_names,
            questions=questions
        )
        print(f"属性问答结果: {result}")
        return True
    except Exception as e:
        print(f"属性问答失败: {str(e)}")
        return False


def test_2d_image_angle_prediction(perception):
    # 测试2D图像角度预测
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]

    try:
        # 执行角度预测
        result = perception.angle_prediction(
            image_type="2D",
            image_url=image_url,
            object_names=object_names
        )
        print(f"角度预测结果: {result}")
        return True
    except Exception as e:
        print(f"角度预测失败: {str(e)}")
        return False


def test_2d_image_grab_point_prediction(perception):
    # 测试2D图像抓取点检测
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]

    try:
        # 执行抓取点检测
        result = perception.grab_point_prediction(
            image_type="2D",
            image_url=image_url,
            object_names=object_names
        )
        print(f"抓取点检测结果: {result}")
        return True
    except Exception as e:
        print(f"抓取点检测失败: {str(e)}")
        return False


def test_2d_image_key_point_prediction(perception):
    # 测试2D图像关键点检测
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]

    try:
        # 执行关键点检测
        result = perception.key_point_prediction(
            image_type="2D",
            image_url=image_url,
            object_names=object_names
        )
        print(f"关键点检测结果: {result}")
        return True
    except Exception as e:
        print(f"关键点检测失败: {str(e)}")
        return False


def test_2d_image_full_perception(perception):
    # 测试2D图像全功能感知
    image_url = "http://gips3.baidu.com/it/u=1821127123,1149655687&fm=3028&app=3028&f=JPEG&fmt=auto?w=720&h=1280"
    object_names = ["bottle", "cup"]
    questions = ["这个物体是什么颜色的？"]

    try:
        # 执行全功能感知
        result = perception.full_perception(
            image_type="2D",
            image_url=image_url,
            object_names=object_names,
            questions=questions
        )
        print(f"全功能感知结果: {result}")
        return True
    except Exception as e:
        print(f"全功能感知失败: {str(e)}")
        return False


def main():
    try:
        # 初始化感知实例
        perception = init_perception()

        # 运行测试
        print("\n=== 测试2D图像检测 ===")
        test_2d_image_detection(perception)

        print("\n=== 测试3D图像验证 ===")
        test_3d_image_validation(perception)

        print("\n=== 测试2D图像分割 ===")
        test_2d_image_split(perception)

        print("\n=== 测试2D图像属性问答 ===")
        test_2d_image_props_describe(perception)

        print("\n=== 测试2D图像角度预测 ===")
        test_2d_image_angle_prediction(perception)

        print("\n=== 测试2D图像抓取点检测 ===")
        test_2d_image_grab_point_prediction(perception)

        print("\n=== 测试2D图像关键点检测 ===")
        test_2d_image_key_point_prediction(perception)

        print("\n=== 测试2D图像全功能感知 ===")
        test_2d_image_full_perception(perception)

    except Exception as e:
        print(f"程序执行失败: {str(e)}")


if __name__ == '__main__':
    main()
