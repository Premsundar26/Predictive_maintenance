from setuptools import setup

package_name = 'predictive_maintenance'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],

    install_requires=['setuptools'],

    zip_safe=True,

    maintainer='Prem Sundar',

    maintainer_email='prem@example.com',

    description='Predictive Maintenance System',

    license='Apache-2.0',

    entry_points={
        'console_scripts': [

            'sensor_node = predictive_maintenance.sensor_node:main',
            'predictor_node = predictive_maintenance.predictor_node:main',
            'logger_node = predictive_maintenance.logger_node:main',
            'alert_node = predictive_maintenance.alert_node:main',
        ],
    },
)