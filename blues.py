from argparse import ArgumentParser as AP
from modules.basicscan import BasicScanning

class _Main:

    def __init__(self):
        pass


def main():
    par = AP(usage="python3 blues.py {MODE} [OPTIONS] | -h, --help", conflict_handler="resolve")
    # Primary options
    par.add_argument('-o', '--output-file', type=str, dest="write_output_data", help="Write data to a file...")

    # First Group: Basic Scanning Functions
    g1 = par.add_argument_group("Basic Scanning", "Basic scanner utilities.")
    g1.add_argument('-1', '--basic-mode', action="store_true", dest="mode_basic_scan", help="Init mode for basic scanning operations.")
    g1.add_argument('-b', '--basic-scan', action="store_true", dest="init_basic_scan", help="Scan for nearby bluetooth enabled devices.")
    g1.add_argument('-s', '--give-services', action='store_true', dest="add_service_scanning", help="Add service scanning to basic scan.")

    args = par.parse_args()

    # Obj. Init
    basic = BasicScanning(scan_for_services=False)

    # Mode 1
    if args.mode_basic_scan:
        if args.init_basic_scan:
            basic.init_basic_scan()

        if args.add_service_scanning:
            b = BasicScanning(scan_for_services=True)
            b.add_service_scanning(); exit(0)


main()