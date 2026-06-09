import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class SensorNode(Node):

    def __init__(self):
        super().__init__('sensor_node')

        self.publisher = self.create_publisher(
            String,
            'robot_health',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_data
        )

    def publish_data(self):

        temp = random.randint(40,100)
        vibration = round(random.uniform(0.1,2.0),2)
        current = round(random.uniform(1.0,10.0),2)

        msg = String()
        msg.data = f"{temp},{vibration},{current}"

        self.publisher.publish(msg)

        self.get_logger().info(
            f"Published: {msg.data}"
        )

def main(args=None):

    rclpy.init(args=args)

    node = SensorNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()