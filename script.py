import argparse
import subprocess

if __name__ == "__main__":

    required_packages = ('fly-admin-dhcp', 'isc-dhcp-server')

    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default='', action='store')
    filename = parser.parse_args().filename

    if filename != '':
        with open(filename, 'r', newline='\n') as requirements_input:
            required_packages = [pkg.rstrip() for pkg in requirements_input.readlines()]

    create_installed_packages = subprocess.run('apt list --installed >installed-packages.txt', shell=True)
    
    with open('installed-packages.txt', 'r', newline='\n') as packages_input:
        installed_packages = [pkg.rstrip() for pkg in packages_input.readlines()]

    report = {package: False for package in required_packages}
    for installed_package in installed_packages:
        for required_package in required_packages:
            if report[required_package]:
                continue
            if required_package in installed_package:
                report[required_package] = True

    report_data = '\n'.join([f'{pkg} - {"SUCCESS" if report[pkg] else "FAILED"}' for pkg in report])
    print(report_data)

    rm = subprocess.run('rm installed-packages.txt', shell=True)
