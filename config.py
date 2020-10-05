class Config:
    # SMTP Credentials
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

    SESSION_DURATION = 5  # DAYS. The period duration to stay logged in

    BATTERY_MIN_VOLTAGE = 10  # value in Volts
    WATER_MAX_LEVEL = 21.5
    GO_OFFLINE_SENSOR_TIME = 1800  # value in seconds
    GO_OFFLINE_VALVE_TIME = 600  # value in seconds
    CHECK_FOR_STATUS_TIME = 10  # value in seconds

    # device settings
    DEVICE_PORT = "/dev/ttyAMA0"
    BAUD_RATE = 9600

    SYSTEM_BATTERY_MIN_VOLTAGE = 11  # value in Volts
    MAIN_SYSTEM_DEVICE_PORT = "/dev/ttyAMA1"