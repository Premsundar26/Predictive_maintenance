import csv
import os

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LoggerNode(Node):

    def __init__(self):

        super().__init__('logger_node')

        self.file_name = 'health_log.csv'

        if not os.path.exists(self.file_name):
            with open(self.file_name,'w',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(
                    ['temperature',
                     'vibration',
                     'current']
                )

        self.subscription = self.create_subscription(
            String,
            'robot_health',
            self.callback,
            10
        )

    def callback(self,msg):

        values = msg.data.split(',')

        with open(
            self.file_name,
            'a',
            newline=''
        ) as file:

            writer = csv.writer(file)

            writer.writerow(values)

def main(args=None):

    rclpy.init(args=args)

    node = LoggerNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()