import bluetooth
from . import dec

class BasicScanning:

    def __init__(self, scan_for_services, file_to_write_to=""):
        self.of = file_to_write_to
        self.srvscan= scan_for_services
        self.dec = dec.Decor()
        self.title_str = "{}\033[01;37m Basic Scan (M/1) Initialized...\033[0m\n" \
                         "{}\033[01;37m Scanning for nearby (BT) Devices...\033[0m\n".format(self.dec.plus_bold(),
                                                                                    self.dec.plus_bold())

    def init_basic_scan(self):
        print(self.title_str)

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