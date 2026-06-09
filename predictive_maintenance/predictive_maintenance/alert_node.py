import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertNode(Node):

    def __init__(self):

        super().__init__('alert_node')

        self.subscription = self.create_subscription(
            String,
            'maintenance_status',
            self.callback,
            10
        )

    def callback(self,msg):

        if msg.data == "MAINTENANCE REQUIRED":

            self.get_logger().warn(
                "ALERT! Maintenance Needed"
            )

def main(args=None):

    rclpy.init(args=args)

    node = AlertNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()