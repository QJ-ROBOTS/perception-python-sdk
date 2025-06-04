import os
import statistics
import time
from concurrent.futures import ThreadPoolExecutor

from dotenv import load_dotenv

from py_qj_robots import Perception

qj_app_id = 'app_j9xr3xp6yxnhgelua8fajtkpgaxb'
qj_app_secret = 'K5vWEe8yH8ZmHf8djL2tNKWjkHCS6QTT'


def init_perception(qj_app_id=None, qj_app_secret=None):
    if qj_app_id and qj_app_secret:
        os.environ['QJ_APP_ID'] = qj_app_id
        os.environ['QJ_APP_SECRET'] = qj_app_secret
    else:
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


def run_stress_test(concurrency, rounds):
    """
    压力测试函数

    :param concurrency: 并发度
    :param rounds: 执行轮次
    :return: 测试报告
    """
    total_requests = concurrency * rounds
    results = []
    success_count = 0
    failure_count = 0
    latencies = []

    def worker():
        nonlocal success_count, failure_count
        for _ in range(rounds):
            start_time = time.time()
            try:
                success, latency = test_2d_image_detection(init_perception(qj_app_id, qj_app_secret))
                latencies.append(latency)
                if success:
                    success_count += 1
                else:
                    failure_count += 1
            except Exception as e:
                failure_count += 1
                latencies.append(0)
                print(f"Error: {e}")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(worker) for _ in range(concurrency)]

        for future in futures:
            future.result()

    end_time = time.time()

    # 计算指标
    total_time = end_time - start_time
    min_latency = min(latencies) if latencies else 0
    max_latency = max(latencies) if latencies else 0
    avg_latency = statistics.mean(latencies) if latencies else 0

    # 耗时分布
    latency_distribution = {
        'lt_3': 0,
        '3_to_5': 0,
        '5_to_10': 0,
        'gt_10': 0
    }

    for latency in latencies:
        if latency < 3:
            latency_distribution['lt_3'] += 1
        elif 3 <= latency < 5:
            latency_distribution['3_to_5'] += 1
        elif 5 <= latency < 10:
            latency_distribution['5_to_10'] += 1
        else:
            latency_distribution['gt_10'] += 1

    # 计算占比
    latency_distribution_percentage = {
        key: (value / total_requests * 100) if total_requests > 0 else 0
        for key, value in latency_distribution.items()
    }

    report = {
        'test_function': 'test_2d_image_detection',
        'rounds': rounds,
        'concurrency': concurrency,
        'total_requests': total_requests,
        'success_count': success_count,
        'failure_count': failure_count,
        'min_latency': min_latency,
        'max_latency': max_latency,
        'avg_latency': avg_latency,
        'latency_distribution': latency_distribution,
        'latency_distribution_percentage': latency_distribution_percentage,
        'total_time': total_time
    }

    return report


if __name__ == '__main__':
    # 示例：执行压力测试，并发度10，执行轮次5
    report = run_stress_test(concurrency=10, rounds=5)

    # 打印测试报告
    print("测试报告:")
    print(f"测试函数名: {report['test_function']}")
    print(f"执行轮次: {report['rounds']}")
    print(f"并发度: {report['concurrency']}")
    print(f"请求次数: {report['total_requests']}")
    print(f"成功次数: {report['success_count']}")
    print(f"失败次数: {report['failure_count']}")
    print(f"最小耗时: {report['min_latency']:.2f} 秒")
    print(f"最大耗时: {report['max_latency']:.2f} 秒")
    print(f"平均耗时: {report['avg_latency']:.2f} 秒")
    print(f"总耗时: {report['total_time']:.2f} 秒")
    print("耗时分布次数及占比:")
    for key, value in report['latency_distribution'].items():
        percentage = report['latency_distribution_percentage'][key]
        print(f"  {key}: {value} 次, {percentage:.2f}%")
