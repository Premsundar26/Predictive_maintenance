import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PredictorNode(Node):

    def __init__(self):

        super().__init__('predictor_node')

        self.subscription = self.create_subscription(
            String,
            'robot_health',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            'maintenance_status',
            10
        )

    def callback(self,msg):

        temp,vibration,current = msg.data.split(',')

        temp = float(temp)
        vibration = float(vibration)
        current = float(current)

        status = "NORMAL"

        if temp > 80:
            status = "MAINTENANCE REQUIRED"

        if vibration > 1.2:
            status = "MAINTENANCE REQUIRED"

        if current > 7:
            status = "MAINTENANCE REQUIRED"

        out = String()
        out.data = status

        self.publisher.publish(out)

        self.get_logger().info(
            f"Prediction: {status}"
        )

def main(args=None):

    rclpy.init(args=args)

    node = PredictorNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()