import bluetooth
from PyOBEX.client import Client
from . import dec

class BasicScanning:

    def __init__(self, device_address="", service_type="", file_to_write_to=""):
        self.deviceaddr = device_address
        self.srv_type = service_type
        self.of = file_to_write_to
        self.port = ""
        self.host = ""
        self.name = ""
        self.dec = dec.Decor()

    def init_basic_scan(self):
        print("{}\033[01;37m Basic Scan (M/1) Initialized...\033[0m\n" \
                         "{}\033[01;37m Scanning for nearby (BT) Devices...\033[0m\n".format(self.dec.plus_bold(),
                                                                                    self.dec.plus_bold()))

        # Init BT Proto
        try:
            devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
            devno = len(devices)

            # Print device number banner
            print("{}\033[37m Found Devices: {}\033[0m\n\n".format(self.dec.astk(), devno))

            for addr, name, dc in devices:
                print(
                    "\t\033[32m++\033[37m Device Name:\t\t\033[0m{}\n"
                    "\t\033[32m++\033[37m Device Address:\t{}\033[0m\n"
                    "\t\033[32m++\033[37m Device Class:\t{}\033[0m\n".format(name, addr, dc)
                )

        except bluetooth.BluetoothError as e:
            pass

    def add_service_scanning(self):
        print("{}\033[01;37m Initializing service scan...\033[0m\n".format(self.dec.astk()))

        try:
            devices = bluetooth.discover_devices(lookup_names=True)
            devno = len(devices)

            for addr, name in devices:
                print("\t\033[32m++\033[37m Service(s) found for {}:{}:\n\033[0m".format(name, addr))

                srv = bluetooth.find_service(address=addr)

                for s in srv:
                    print("\t\033[01;33m[{}]\n\033[0m".format(s['name']))

        except bluetooth.BluetoothError as e:
            pass

    def scan_device_for_service(self):
        print("{}\033[01;37m Scanning {}\033[0m\n"
              "{}\033[01;37m Service Lookup: \033[01;33m{}\033[0m".format(self.dec.astk(), self.deviceaddr, self.dec.astk(), self.srv_type))

        smt = bluetooth.find_service(name=str(b'{}\x00').format(self.srv_type), address=self.deviceaddr)

        # Check if the service exists on the device
        if len(smt) == 0:
            print("\n\033[31mService \"{}\" does not exist on address {}...\033[0m\n".format(self.srv_type, self.deviceaddr))
            exit(1)
        else:
            fm = smt[0]
            self.port = fm["port"]
            self.name = fm["name"]
            self.host = fm["host"]

            print("{}\033[01;37m Checking connection to {} through {}...\n".format(self.dec.astk(), self.deviceaddr, self.srv_type))
            client = Client(self.host, self.port)
            try:
                client.connect()
                print("{}\033[01;37m Connection through {} was successful, {} is usable!".format(self.dec.plus_bold(), self.srv_type, self.srv_type))
                client.disconnect()
            except bluetooth.BluetoothError as e:
                pass